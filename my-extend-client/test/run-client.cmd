SETLOCAL

cd ..

mvn exec:java -Dtangosol.coherence.cacheconfig=.\test\extend-cache-config.xml


ENDLOCAL