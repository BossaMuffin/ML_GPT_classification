#!/usr/bin/env python3
# coding: utf-8
"""
Created on January 20th, 2023
@title: Clusters' Topics by GPT
@version: 2
@author: Balthazar Méhus
@society: CentraleSupélec
@abstract: Nommer une liste de mots par une expression le représentant le mieux possible - argues manager
"""

import argparse


class Args:

    def __init__(self):
        self.AVAILABLE_MODELS = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]
        self.AVAILABLE_TEMPERATURE = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.7, 0.8, 0.9, 1]
        self.DEFAULT_DOMAIN = "artificial intelligence"
        self.DEFAULT_TEMPERATURE = 0

        self._parser = argparse.ArgumentParser(
            prog="Clusters' Topics by GPT",
            description="""Nommer une liste de mots par une expression le représentant le mieux possible.""",
            epilog="""
            By Balthazar Mehus /
            MS SIO 22-23 /
            CentraleSupélec
            -> See the README file and Have fun ;)
            """
        )
        self._parser.add_argument(dest="words",
                                  type=str,
                                  nargs=1,
                                  help="A string which is a list of words separated by a coma.")

        self._parser.add_argument("-m",
                                  "--model",
                                  dest="model",
                                  type=str,
                                  required=False,
                                  default=self.AVAILABLE_MODELS[1],
                                  choices=self.AVAILABLE_MODELS,
                                  help="[Optional] The model that you want to use.")

        self._parser.add_argument("-t",
                                  "--temperature",
                                  dest="temperature",
                                  type=float,
                                  required=False,
                                  default=0,
                                  choices=self.AVAILABLE_TEMPERATURE,
                                  help="[Optional] The value of the temperature to set the model "
                                       "(see the README), from 0 to 1.")

        self._parser.add_argument("-d",
                                  "--domain",
                                  dest="domain",
                                  type=str,
                                  required=False,
                                  default=self.DEFAULT_DOMAIN,
                                  help="[Optional] The domain to set the context assistant.")

        self.parsed_args = self._parser.parse_args()
