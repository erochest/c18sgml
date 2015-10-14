module Main where


import           Control.Error

import           C18.Actions

import           Opts


main :: IO ()
main = runScript . action =<< parseActions
