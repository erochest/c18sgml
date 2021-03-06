module C18.Actions.Report where


import           Data.Foldable
import qualified Data.Set          as S
import qualified Data.Text.IO      as TIO
import           System.IO
import           Text.HTML.TagSoup

import           Control.Error

import           C18.Balance
import           C18.Types


report :: Script ()
report = scriptIO
         . mapM_ TIO.putStrLn
         . imbalancedTags
         . foldl' trackTag (TagStack [] S.empty)
         . parseTags
       =<< scriptIO (TIO.hGetContents stdin)
