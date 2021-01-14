__author__ = 'chandra'

import re
import traceback
from logsetup import logger


def get_refined_interpretations(input_string):
    keywords = ['Genetic Variant', 'Positive', 'Significant Mutation']
    status = 'NEGATIVE'

    try:
        if any(word.upper() in str(input_string).upper() for word in keywords):
            status = 'POSITIVE'

        return status

    except:
        status_message = 'ERROR : Error occurred while preparing data for HBase.\nERROR in ', locals(), ' while running. ERROR MESSAGE: ' + str(
            traceback.format_exc())
        logger.error(status_message)
        return


def get_refined_results(input_string):
    non_alpha_regex = r'\W'
    non_alpha_pat = re.compile(non_alpha_regex)
    keywords = ['Deleterious', 'positive']
    result = None

    try:
        for word in keywords:
            if str(input_string).upper().__contains__(word.upper()):
                result = word

        else:
            result = re.sub(r'\W', '', input_string)

        return result

    except:
        status_message = 'ERROR : Error occurred while preparing data for HBase.\nERROR in ', locals(), ' while running. ERROR MESSAGE: ' + str(
            traceback.format_exc())
        logger.error(status_message)
        return
