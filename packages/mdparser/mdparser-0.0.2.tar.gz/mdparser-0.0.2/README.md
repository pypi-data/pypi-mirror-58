## mdparser
   **实现将一个 md 文档项目 转换 --> 保存到 mysql 数据库的这一过程**

   ---

## 文件目录的组织形式
   **为了方便解析，mdparser 要求目录要满足如下要求**

   |**类型**|**要求**|
   |-------|--------|
   |目录    | **blogs~blog-group-id~blog-group-name**|
   |目录    | **books~book-id~book-name**|
   |博客文件 | **blog-id~blog-name.md**|
   |文章文件 | **article-id~article-name.md**|

   ---

   ```bash
tree ./
./
├── blogs~1~python多线程
└── books~1~numpy入门
    └── 1~ndarray的那些事.md
   ```
