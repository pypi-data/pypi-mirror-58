import sys
from time import sleep
import concurrent.futures as confu
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Any, Dict

from pyinsights.aws import InsightsClient
from pyinsights.config import load_config, validate
from pyinsights.formatter import format_result
from pyinsights.helper import get_times, processing


def query(params: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Query to CloudWatch Logs Insights

    Arguments:
        params {Dict[str, Dict[str, Any]]}

    Returns:
        results {Dict[str, Any]}
    """

    client = InsightsClient(region=params['region'], profile=params['profile'])
    client.start_query(**params['config'])
    results = client.fetch_result()
    return results


def run_thread(params: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Run thread

    Arguments:
        params {Dict[str, Dict[str, Any]]}

    Returns:
        results = Dict[str, Any]
    """

    with ThreadPoolExecutor(max_workers=1) as executor:
        thread = executor.submit(query, params)
        processing('Waiting', end=' ')

        while True:
            try:
                results = thread.result(timeout=0.1)
            except confu.TimeoutError:
                processing('.', end='')
                sleep(0.5)
                pass
            else:
                if results:
                    processing('.', end='\n')
                    break

    return results


def run(kwargs: Dict[str, str]) -> bool:
    """Run pyinsights

    Arguments:
        kwargs {Dict[str, Any]}

    Returns:
        bool
    """

    format_type = kwargs.pop('format')
    config = load_config(kwargs['config'])
    validate(config)
    kwargs['config'] = config
    duration = config.pop('duration')
    duration = get_times(duration)
    kwargs['config'].update(duration)

    results = run_thread(kwargs)
    formatted_result = format_result(format_type, results['results'])
    sys.stdout.write(formatted_result)

    return True
