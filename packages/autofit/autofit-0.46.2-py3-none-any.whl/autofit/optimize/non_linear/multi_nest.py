import logging

import numpy as np
import pymultinest

from autofit import conf, exc
from autofit.optimize.non_linear.output import Output
from autofit.optimize.non_linear.non_linear import NonLinearOptimizer
from autofit.optimize.non_linear.non_linear import Result
from autofit.optimize.non_linear.non_linear import persistent_timer

logger = logging.getLogger(__name__)


class MultiNest(NonLinearOptimizer):
    def __init__(self, paths, sigma_limit=3, run=pymultinest.run):
        """
        Class to setup and run a MultiNest lens and output the MultiNest nlo.

        This interfaces with an input model_mapper, which is used for setting up the \
        individual model instances that are passed to each iteration of MultiNest.
        """

        super().__init__(paths)

        self.sigma_limit = sigma_limit

        self.importance_nested_sampling = self.config(
            "importance_nested_sampling", bool
        )
        self.multimodal = self.config("multimodal", bool)
        self.const_efficiency_mode = self.config("const_efficiency_mode", bool)
        self.n_live_points = self.config("n_live_points", int)
        self.evidence_tolerance = self.config("evidence_tolerance", float)
        self.sampling_efficiency = self.config("sampling_efficiency", float)
        self.n_iter_before_update = self.config("n_iter_before_update", int)
        self.null_log_evidence = self.config("null_log_evidence", float)
        self.max_modes = self.config("max_modes", int)
        self.mode_tolerance = self.config("mode_tolerance", float)
        self.outputfiles_basename = self.config("outputfiles_basename", str)
        self.seed = self.config("seed", int)
        self.verbose = self.config("verbose", bool)
        self.resume = self.config("resume", bool)
        self.context = self.config("context", int)
        self.write_output = self.config("write_output", bool)
        self.log_zero = self.config("log_zero", float)
        self.max_iter = self.config("max_iter", int)
        self.init_MPI = self.config("init_MPI", bool)
        self.run = run

        logger.debug("Creating MultiNest NLO")

    def copy_with_name_extension(self, extension, remove_phase_tag=False):
        copy = super().copy_with_name_extension(
            extension=extension, remove_phase_tag=remove_phase_tag
        )
        copy.sigma_limit = self.sigma_limit
        copy.run = self.run
        copy.importance_nested_sampling = self.importance_nested_sampling
        copy.multimodal = self.multimodal
        copy.const_efficiency_mode = self.const_efficiency_mode
        copy.n_live_points = self.n_live_points
        copy.evidence_tolerance = self.evidence_tolerance
        copy.sampling_efficiency = self.sampling_efficiency
        copy.n_iter_before_update = self.n_iter_before_update
        copy.null_log_evidence = self.null_log_evidence
        copy.max_modes = self.max_modes
        copy.mode_tolerance = self.mode_tolerance
        copy.outputfiles_basename = self.outputfiles_basename
        copy.seed = self.seed
        copy.verbose = self.verbose
        copy.resume = self.resume
        copy.context = self.context
        copy.write_output = self.write_output
        copy.log_zero = self.log_zero
        copy.max_iter = self.max_iter
        copy.init_MPI = self.init_MPI
        return copy

    class Fitness(NonLinearOptimizer.Fitness):
        def __init__(
            self, paths, analysis, instance_from_physical_vector, output_results
        ):
            super().__init__(paths, analysis, output_results)
            self.instance_from_physical_vector = instance_from_physical_vector
            self.accepted_samples = 0

            self.model_results_output_interval = conf.instance.general.get(
                "output", "model_results_output_interval", int
            )
            self.stagger_resampling_likelihood = conf.instance.non_linear.get(
                "MultiNest", "stagger_resampling_likelihood", bool
            )
            self.stagger_resampling_value = conf.instance.non_linear.get(
                "MultiNest", "stagger_resampling_value", float
            )
            self.resampling_likelihood = conf.instance.non_linear.get(
                "MultiNest", "null_log_evidence", float
            )
            self.stagger_accepted_samples = 0

        def __call__(self, cube, ndim, nparams, lnew):

            try:
                instance = self.instance_from_physical_vector(cube)
                likelihood = self.fit_instance(instance)
            except exc.FitException:

                if not self.stagger_resampling_likelihood:
                    likelihood = -np.inf
                else:

                    if self.stagger_accepted_samples < 10:

                        self.stagger_accepted_samples += 1
                        self.resampling_likelihood += self.stagger_resampling_value
                        likelihood = self.resampling_likelihood

                    else:

                        likelihood = -1.0 * np.abs(self.resampling_likelihood) * 10.0

            return likelihood

    @persistent_timer
    def fit(self, analysis, model):
        multinest_output = Output(model, self.paths)

        multinest_output.save_model_info()

        # noinspection PyUnusedLocal
        def prior(cube, ndim, nparams):

            # NEVER EVER REFACTOR THIS LINE!

            phys_cube = model.physical_vector_from_hypercube_vector(
                hypercube_vector=cube
            )

            for i in range(len(phys_cube)):
                cube[i] = phys_cube[i]

            return cube

        fitness_function = MultiNest.Fitness(
            self.paths,
            analysis,
            model.instance_from_physical_vector,
            multinest_output.output_results,
        )

        logger.info("Running MultiNest...")
        self.run(
            fitness_function.__call__,
            prior,
            model.prior_count,
            outputfiles_basename="{}/multinest".format(self.paths.path),
            n_live_points=self.n_live_points,
            const_efficiency_mode=self.const_efficiency_mode,
            importance_nested_sampling=self.importance_nested_sampling,
            evidence_tolerance=self.evidence_tolerance,
            sampling_efficiency=self.sampling_efficiency,
            null_log_evidence=self.null_log_evidence,
            n_iter_before_update=self.n_iter_before_update,
            multimodal=self.multimodal,
            max_modes=self.max_modes,
            mode_tolerance=self.mode_tolerance,
            seed=self.seed,
            verbose=self.verbose,
            resume=self.resume,
            context=self.context,
            write_output=self.write_output,
            log_zero=self.log_zero,
            max_iter=self.max_iter,
            init_MPI=self.init_MPI,
        )
        logger.info("MultiNest complete")

        # TODO: Some of the results below use the backup_path, which isnt updated until the end if thiss function is
        # TODO: not located here. Do we need to rely just ono the optimizer foldeR? This is a good idea if we always
        # TODO: have a valid sym-link( e.g. even for aggregator use).

        self.paths.backup()
        instance = multinest_output.most_likely_model_instance
        analysis.visualize(instance=instance, during_analysis=False)
        multinest_output.output_results(during_analysis=False)
        multinest_output.output_pdf_plots()
        result = Result(
            instance=instance,
            figure_of_merit=multinest_output.evidence,
            previous_model=model,
            gaussian_tuples=multinest_output.gaussian_priors_at_sigma_limit(
                self.sigma_limit
            ),
        )
        self.paths.backup_zip_remove()
        return result
