srcD=/home/pi/OneDrive/techblog
dstD=/home/pi/techblogcp

override="scaffolds source themes _config.yml package.json package-lock.json"

for x in $override
  do
  rm -r $dstD/$x
  ln -s $srcD/$x $dstD
  done
