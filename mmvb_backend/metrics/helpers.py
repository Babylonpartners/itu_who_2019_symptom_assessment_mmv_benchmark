from metrics.implementations import SUPPORTED_METRICS

METRICS_IDS = list(SUPPORTED_METRICS)


def calculate_metrics(benchmark_session_result, metrics=METRICS_IDS):
    """Calculates the selected or the available metrics for a given benchmark result"""
    calculated_metrics = []

    for metric_id in metrics:
        metric_implementation = SUPPORTED_METRICS[metric_id]
        calculated_metric = metric_implementation.calculate(
            benchmark_session_result
        )
        calculated_metric = metric_implementation.aggregate(calculated_metric)
        calculated_metrics.append(calculated_metric)

    return calculated_metrics
