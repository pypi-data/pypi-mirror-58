# -*- coding: utf-8 -*-

from nwae.config.Config import Config
from nwae.utils.Log import Log
from inspect import getframeinfo, currentframe
import nwae.lib.lang.LangFeatures as lf
from nwae.lib.lang.preprocessing.TrDataPreprocessor import TrDataPreprocessor
from nwae.utils.UnitTest import ResultObj
import pandas as pd
from nwae.samples.SampleTextClassificationData import SampleTextClassificationData
from nwae.lib.lang.nlp.daehua.DaehuaTrainDataModel import DaehuaTrainDataModel


class UtTrDataPreprocessor:

    def __init__(
            self,
            config
    ):
        self.config = config
        return

    def run_unit_test_lang(
            self,
            lang
    ):
        sample_data = SampleTextClassificationData.get_text_classification_training_data(
            lang = lang,
            type_io = SampleTextClassificationData.TYPE_IO_IN
        )
        expected_output_data = SampleTextClassificationData.get_text_classification_training_data(
            lang = lang,
            type_io = SampleTextClassificationData.TYPE_IO_OUT
        )

        fake_training_data = pd.DataFrame({
            DaehuaTrainDataModel.COL_TDATA_INTENT_ID: sample_data[SampleTextClassificationData.COL_CLASS],
            DaehuaTrainDataModel.COL_TDATA_INTENT_NAME: sample_data[SampleTextClassificationData.COL_CLASS_NAME],
            DaehuaTrainDataModel.COL_TDATA_TEXT: sample_data[SampleTextClassificationData.COL_TEXT],
            DaehuaTrainDataModel.COL_TDATA_TRAINING_DATA_ID: sample_data[SampleTextClassificationData.COL_TEXT_ID],
            # Don't do any processing until later
            DaehuaTrainDataModel.COL_TDATA_TEXT_SEGMENTED: None
        })
        Log.debug('Fake Training Data:\n\r' + str(fake_training_data))
        Log.debug('Expected Output:\n\r' + str(expected_output_data))

        ctdata = TrDataPreprocessor(
            model_identifier     = str(lang) + ' Test Training Data Text Processor',
            language             = lang,
            df_training_data     = fake_training_data,
            dirpath_wordlist     = self.config.get_config(param=Config.PARAM_NLP_DIR_WORDLIST),
            postfix_wordlist     = self.config.get_config(param=Config.PARAM_NLP_POSTFIX_WORDLIST),
            dirpath_app_wordlist = self.config.get_config(param=Config.PARAM_NLP_DIR_APP_WORDLIST),
            postfix_app_wordlist = self.config.get_config(param=Config.PARAM_NLP_POSTFIX_APP_WORDLIST),
            dirpath_synonymlist  = self.config.get_config(param=Config.PARAM_NLP_DIR_SYNONYMLIST),
            postfix_synonymlist  = self.config.get_config(param=Config.PARAM_NLP_POSTFIX_SYNONYMLIST),
            reprocess_all_text   = True,
        )

        ctdata.go()

        Log.debug('*********** FINAL SEGMENTED DATA (' + str(ctdata.df_training_data.shape[0]) + ' sentences)')
        Log.debug(ctdata.df_training_data.columns)
        Log.debug(ctdata.df_training_data.values)

        Log.debug('*********** ROWS CHANGED ***********')
        count = 0
        for row in ctdata.list_of_rows_with_changed_processed_text:
            count += 1
            Log.debugdebug(str(count) + '. ' + str(row))

        # Compare results
        expected_text_segmented = expected_output_data[SampleTextClassificationData.COL_TEXT_SEG]
        Log.debugdebug(expected_text_segmented)
        res_text_segmented = ctdata.df_training_data[DaehuaTrainDataModel.COL_TDATA_TEXT_SEGMENTED].tolist()
        Log.debugdebug(res_text_segmented)
        res_obj = ResultObj(
            count_ok = 0,
            count_fail = 0
        )
        if len(expected_text_segmented) != len(res_text_segmented):
            raise Exception(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Expected array length ' + str(len(expected_text_segmented))
                + ' != output array length ' + str(len(res_text_segmented))
            )
        for i in range(len(expected_text_segmented)):
            b = expected_text_segmented[i] == res_text_segmented[i]
            res_obj.count_ok += 1*b
            res_obj.count_fail += 1*(not b)
            if b == False:
                Log.error(
                    str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': Error "' + str(res_text_segmented[i]) + '", expected "' + str(expected_text_segmented[i])
                )

        Log.important(
            '***** Training Data Preprocessor ' + str(lang) + ' PASSED ' + str(res_obj.count_ok)
            + ', FAILED ' + str(res_obj.count_fail) + ' *****'
        )
        return res_obj

    def run_unit_test(self):
        all_res = ResultObj(count_ok=0, count_fail=0)
        for lang in [lf.LangFeatures.LANG_VN, lf.LangFeatures.LANG_TH, lf.LangFeatures.LANG_CN]:
            res = self.run_unit_test_lang(lang = lang)
            all_res.count_ok += res.count_ok
            all_res.count_fail += res.count_fail
        return all_res


if __name__ == '__main__':
    config = Config.get_cmdline_params_and_init_config_singleton(
        Derived_Class=Config,
        default_config_file='/usr/local/git/nwae/nwae/app.data/config/local.nwae.cf'
    )

    Log.LOGLEVEL = Log.LOG_LEVEL_DEBUG_1
    UtTrDataPreprocessor(config).run_unit_test()
