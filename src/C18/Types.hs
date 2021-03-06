{-# LANGUAGE DeriveDataTypeable #-}
{-# LANGUAGE DeriveGeneric      #-}


module C18.Types where


import           Data.Data
import qualified Data.Set     as S
import qualified Data.Text    as T
import           GHC.Generics


-- TODO: Have the input of `DeNest` translate into a `DeNestTransform`.
data Actions
    = Report
    | DeNest
    { denestInput     :: !FilePath
    , denestOutput    :: !FilePath
    , denestTagNames  :: !(S.Set T.Text)
    , denestEmptyTags :: !(S.Set T.Text)
    } deriving (Show, Eq, Data, Typeable, Generic)

data TagStack a
    = TagStack
    { stack          :: [a]
    , imbalancedTags :: S.Set a
    } deriving (Eq, Show)

data DeNestTransform
    = DeNestTrans
    { denestTags  :: !(S.Set T.Text)
    , denestEmpty :: !(S.Set T.Text)
    } deriving (Eq, Show)
