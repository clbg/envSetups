sudo apt-get install -y nodejs
sudo apt-get install -y npm
sudo apt-get install -y nodejs-legacy 
npm -v
sudo npm install -g hexo-cli --no-optional

hexo init ~/blog
hexo init ~/techblog

echo "SOURCE BLOG PATH:"
echo  $BLOG

echo "SOURCE TECH BLOG PATH:"
echo $TECH_BLOG

blogdst=~/blog
techblogdst=~/techblog

override="scaffolds source themes _config.yml package.json package-lock.json"

for x in $override
  do
  rm -r $blogdst/$x
  ln -s $BLOG/$x $blogdst

  rm -r $techblogdst/$x
  ln -s $TECH_BLOG/$x $techblogdst
  done
