module C18.Actions.DeNest where


import           Control.Error
import qualified Data.Set          as S
import qualified Data.Text         as T
import qualified Data.Text.IO      as TIO
import           Data.Traversable
import           Text.HTML.TagSoup

import           C18.Balance
import           C18.Types


deNest :: FilePath -> FilePath -> S.Set T.Text -> S.Set T.Text -> Script ()
deNest inputFile outputFile tagNames emptyTags =
    scriptIO . TIO.writeFile outputFile
                 . renderTags
                 . concat
                 . snd
                 . mapAccumL (denestTag trans) []
                 . parseTags
        =<< scriptIO (TIO.readFile inputFile)
    where
      trans = DeNestTrans tagNames emptyTags
