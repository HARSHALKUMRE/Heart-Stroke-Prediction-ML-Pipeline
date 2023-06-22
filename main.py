import os, sys
import pandas as pd
import numpy as np
from heart_stroke.constant import *
from heart_stroke.logger import logging
from heart_stroke.exception import HeartStrokeException
from heart_stroke.pipeline.training_pipeline import TrainingPipeline

def main():
    try:
        pipeline = TrainingPipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")


if __name__ == '__main__':
    main()