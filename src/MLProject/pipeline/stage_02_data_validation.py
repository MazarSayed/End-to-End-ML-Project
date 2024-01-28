from MLProject.config.configuration import ConfigurationManager
from MLProject.components.data_validation import DataValidation
from MLProject import logger


STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
 def __inti__(Self):
  pass

 def main(Self):
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(config=data_validation_config)
    data_validation.validate_all_columns()

if __name__ == '__main__': 
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e