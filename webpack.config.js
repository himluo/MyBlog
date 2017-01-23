var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var CommonsChunkPlugin = webpack.optimize.CommonsChunkPlugin;

module.exports = {
  context: __dirname,
  entry: {
      blogs: './blogs/entrys/blogs.js',
      blog: './blogs/entrys/blog.js',
  },//entry文件的位置
  output: {
      path: path.resolve('./blogs/dist/'), //和settings.py里的WEBPACK_LOADER的设置对应
      filename: "[name].bundle.js",
  },

  plugins: [
      new CommonsChunkPlugin({
          name: "pager-commons",
          chunks: ["blogs", "blog"],
      }),
      new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: { //使用babel loader
      loaders: [
      {
          test: /\.vue$/,
          loader: 'vue',

      },
      {
          test: /\.js$/,
          exclude: /node_modules|vue\/dist|vue-loader\/|vue-hot-reload-api\//,
          loader: 'babel',
      },
    ]
  },
  babel: {
      presets: ['es2015']
  },

  resolve: {
      modulesDirectories: ['node_modules', 'bower_components'],
      extensions: ['', '.js', '.jsx'],
      alias: {
            'vue$'  : 'vue/dist/vue.min'
        }
  },

};