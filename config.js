/* ============================================================
   施工工艺样板 · 只改这个文件
   一条 = 一个工艺 = 一张贴现场的二维码
   ============================================================ */

/* 换照片后把这个数字 +1，否则微信会一直显示旧图 */
window.VERSION = '1';

/* 部署后的网址，生成二维码前填真实地址
   GitHub Pages 格式： https://用户名.github.io/仓库名   （末尾不要加 /） */
window.SITE_URL = 'https://用户名.github.io/仓库名';

/* 顶部小字（所有工艺共用），不需要就写 '' */
window.SITE_TITLE = '施工工艺样板';

/* ============================================================
   工艺列表 —— 下面是我编的示例，你按实际改：
   改 name（工艺名）、images（照片路径）
   加工艺：复制一整段 { ... }, 粘贴到下面
   删工艺：把对应的整段删掉

   ---------- 照片后面那一屏二维码（可选）----------
   方式 A（推荐）：写 link，页面会自动把网址变成二维码
        link: 'https://某个网站.com/xxx'
        工人长按识别 -> 打开这个网站
        下面还会多一个「直接打开」按钮，长按没反应时点它

   方式 B：写 qr，用你自己已有的二维码截图
        qr: 'img/rebar-qr.png'
        把截图放进 img 目录，路径写在这里

   两个都不写 -> 只有照片，没有这一屏
   ============================================================ */
window.ITEMS = [
  {
    id: 'rebar',
    name: '钢筋绑扎',
    images: [
      'img/rebar/1.jpg',
      'img/rebar/2.jpg',
      'img/rebar/3.jpg'
    ],
    link: 'https://example.com/rebar'   // ← 末尾二维码指向的网址，删掉这行就没有那一屏
  },

  {
    id: 'formwork',
    name: '模板支设',
    images: [
      'img/formwork/1.jpg',
      'img/formwork/2.jpg',
      'img/formwork/3.jpg'
    ],
    link: 'https://example.com/formwork'
  },

  {
    id: 'concrete',
    name: '混凝土浇筑',
    images: [
      'img/concrete/1.jpg',
      'img/concrete/2.jpg',
      'img/concrete/3.jpg'
    ],
    link: 'https://example.com/concrete'
  },

  {
    id: 'masonry',
    name: '砌体工程',
    images: [
      'img/masonry/1.jpg',
      'img/masonry/2.jpg',
      'img/masonry/3.jpg'
    ],
    link: 'https://example.com/masonry'
  },

  {
    id: 'waterproof',
    name: '防水工程',
    images: [
      'img/waterproof/1.jpg',
      'img/waterproof/2.jpg',
      'img/waterproof/3.jpg'
    ],
    link: 'https://example.com/waterproof'
  }
];
