/* ============================================================
   施工工艺样板 · 只改这个文件
   一条 = 一个工艺 = 一张贴现场的二维码
   ============================================================ */

/* 换照片后把这个数字 +1，否则微信会一直显示旧图 */
window.VERSION = '1';

/* 部署后的网址，生成二维码前填真实地址 */
window.SITE_URL = 'https://你的域名.edgeone.app';

/* 顶部小字（所有工艺共用），不需要就写 '' */
window.SITE_TITLE = '施工工艺样板';

/* ============================================================
   工艺列表 —— 下面是我编的示例，你按实际改：
   改 name（工艺名）、images（照片路径）
   加工艺：复制一整段 { ... }, 粘贴到下面
   删工艺：把对应的整段删掉
   
   最后一行的 qr 是可选的：
   填了 -> 图片后面多一屏二维码（长按识别）
   不填 -> 就只有照片，没有那一屏
   ============================================================ */
window.ITEMS = [
  {
    id: 'rebar',
    name: '钢筋绑扎',
    images: [
      'img/rebar/1.jpg',
      'img/rebar/2.jpg',
      'img/rebar/3.jpg'
    ]
  },

  {
    id: 'formwork',
    name: '模板支设',
    images: [
      'img/formwork/1.jpg',
      'img/formwork/2.jpg',
      'img/formwork/3.jpg'
    ]
  },

  {
    id: 'concrete',
    name: '混凝土浇筑',
    images: [
      'img/concrete/1.jpg',
      'img/concrete/2.jpg',
      'img/concrete/3.jpg'
    ]
  },

  {
    id: 'masonry',
    name: '砌体工程',
    images: [
      'img/masonry/1.jpg',
      'img/masonry/2.jpg',
      'img/masonry/3.jpg'
    ]
  },

  {
    id: 'waterproof',
    name: '防水工程',
    images: [
      'img/waterproof/1.jpg',
      'img/waterproof/2.jpg',
      'img/waterproof/3.jpg'
    ]
  }
];
