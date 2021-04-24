{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
module Paths_1291C (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/torsho/.cabal/bin"
libdir     = "/home/torsho/.cabal/lib/x86_64-linux-ghc-8.6.5/1291C-0.1.0.0-GD3D1Rd05TsKo5jLbcrm94-1291C"
dynlibdir  = "/home/torsho/.cabal/lib/x86_64-linux-ghc-8.6.5"
datadir    = "/home/torsho/.cabal/share/x86_64-linux-ghc-8.6.5/1291C-0.1.0.0"
libexecdir = "/home/torsho/.cabal/libexec/x86_64-linux-ghc-8.6.5/1291C-0.1.0.0"
sysconfdir = "/home/torsho/.cabal/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "1291C_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "1291C_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "1291C_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "1291C_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "1291C_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "1291C_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
