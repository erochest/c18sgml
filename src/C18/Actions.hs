{-# LANGUAGE RecordWildCards #-}


module C18.Actions where


import           Control.Error

import           C18.Actions.DeNest
import           C18.Actions.Report
import           C18.Types


action :: Actions -> Script ()
action Report       = report
action DeNest{..}   = deNest denestInput denestOutput denestTagNames
                      denestEmptyTags
