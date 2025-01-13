
// 这行代码从 vite 包中导入了 defineConfig 函数。defineConfig 是 Vite 提供的一个辅助函数，
// 用于定义 Vite 配置对象。使用 defineConfig 有几个好处：

// 类型检查：它允许 TypeScript 对配置对象进行类型检查，确保配置的正确性。
// 智能提示：在 IDE 中，使用 defineConfig 可以获得配置选项的智能提示，提高开发效率。
// 性能优化：Vite 可能会在未来的版本中利用 defineConfig 进行一些性能优化，
// 尽管这在当前版本中可能并不明显。
import { defineConfig } from 'vite'


// 这行代码从 @vitejs/plugin-vue 包中导入了 Vue 插件。
// 这个插件是 Vite 官方提供的，用于支持 Vue 3 项目的构建和开发。
// 它提供了对 .vue 文件的处理，包括模板编译、样式处理、脚本转换等。
import vue from '@vitejs/plugin-vue'

// 这行代码从 Node.js 的内置 path 模块中导入了 path 对象。
// path 模块提供了一些实用工具函数，用于处理文件和目录的路径。
import path from 'path'


// Vite 配置文件的导出，使用 defineConfig 函数来定义配置对象
export default defineConfig({
  // 插件配置
  plugins: [vue()], // 引入并使用 Vue 插件，支持 Vue 文件的处理

  // 解析配置
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'), // 设置别名 '@'，指向项目的 'src' 目录，方便在项目中引用 src 目录下的文件
    },
  },

  // 开发服务器配置
  server: {
    port: 3000, // 自定义开发服务器的端口号为 3000，Vite 默认使用其他端口（如 5000 或随机端口）
    host: '0.0.0.0', // 设置开发服务器的主机地址为 '0.0.0.0'，允许外部设备访问。如果只想在本地访问，可以设置为 'localhost'
    open: true, // 启动开发服务器时自动打开浏览器窗口，访问应用
    cors: true, // 允许跨域请求，这对于在开发过程中调用位于不同域名的 API 很有用
  },

  // 构建配置
  build: {
    outDir: 'dist', // 自定义输出目录为 'dist'，Vite 默认也会使用这个目录
    rollupOptions: {
      // Rollup 打包工具的额外配置
      external: ['vue', 'axios'], // 将 'vue' 和 'axios' 配置为外部依赖，意味着在打包时不会将它们包含在内，而是期望它们在运行时通过 CDN 或其他方式提供
      output: {
        // 自定义输出文件的命名和格式
        chunkFileNames: 'assets/[name].[hash].js', // 非入口文件的命名规则，使用哈希值来避免缓存问题
        entryFileNames: 'assets/[name].[hash].js', // 入口文件的命名规则，同样使用哈希值
        assetFileNames: 'assets/[name].[hash].[extname]', // 静态资源的命名规则，如图片、字体等，也使用哈希值
      },
    },
  },

  // esbuild 配置（如果 Vite 使用 esbuild 进行转换）
  esbuild: {
    target: 'es2020', // 设置 esbuild 的目标 JavaScript 版本为 ES2020，确保转换后的代码兼容该版本的浏览器
    // 注意：esbuild 的配置选项可能会随着 Vite 的更新而变化，具体请参考 Vite 和 esbuild 的官方文档
  },

  // 其他可能的配置选项...
  // 这里可以添加 Vite 支持的其他配置选项，如 css、optimizeDeps、devtools 等
  // 具体配置请参考 Vite 的官方文档：https://vite.dev/config/
})