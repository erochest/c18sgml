{-# LANGUAGE OverloadedStrings #-}


module Main where


import           Conduit
import           Data.Foldable
import qualified Data.Text     as T
import qualified Data.Text.IO  as TIO

import           C18.Balance
import           C18.Types


main :: IO ()
main = do
  imbalance <- fmap imbalancedTags . runResourceT $ stdinC $$ balanceReport
  mapM_ (TIO.putStrLn . T.pack . show) $ toList imbalance
