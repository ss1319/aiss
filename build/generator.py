# -*- coding: utf-8 -*-
"""AI配置教程全站生成器 v2 - 全CDN库引入 + 聚合搜索 + 新链接"""
import os

BASE = r"E:\000000已设计好的完整HTML源码\AI配置教程"

# ========== 去重后的CSS库（约54个）==========
CSS_CDN = """
<!-- ===== 编辑器CSS ===== -->
<link rel="stylesheet" href="https://cdn.tiny.cloud/1/no-api-key/tinymce/6.8.3/tinymce.min.css">
<link rel="stylesheet" href="https://cdn.quilljs.com/1.3.7/quill.snow.css">
<link rel="stylesheet" href="https://unpkg.com/wangeditor@4.7.15/dist/css/wangEditor.min.css">
<!-- ===== CSS框架CSS ===== -->
<link rel="stylesheet" href="https://cdn.tailwindcss.com">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/element-plus/dist/index.css">
<!-- ===== 动画CSS ===== -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/textillate@0.4.0/assets/animate.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gradient-animations@1.2.0/dist/gradient-anim.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/border-animations@1.1.0/dist/border-anim.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glow-effects@1.1.0/dist/glow.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/page-transitions@1.3.0/dist/transitions.min.css">
<!-- ===== 组件CSS ===== -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.6.1/cropper.min.css">
<link href="https://vjs.zencdn.net/8.6.1/video-js.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightgallery.js/1.4.0/css/lightgallery.min.css">
<link rel="stylesheet" href="https://cdn.plyr.io/3.6.12/plyr.css">
<link rel="stylesheet" href="https://www.jeasyui.com/easyui/themes/default/easyui.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/handsontable@13.1.0/dist/handsontable.full.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@jaames/iro@5.5.2/dist/iro.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/codemirror@5.65.16/lib/codemirror.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tippy.js@6.3.7/dist/tippy.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/simplebar@6.2.5/dist/simplebar.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/custom-scrollbar-css@4.2.0/dist/custom-scrollbar.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/nanoscroller@0.8.7/bin/css/nanoscroller.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/toolbar.css@1.2.0/dist/toolbar.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/editor-toolbar-kit@1.0.0/dist/toolbar.min.css">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/vue-flow@1.38.1/dist/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/form-designer-vue3@1.2.0/dist/style.css">
<!-- ===== 边框/按钮效果CSS ===== -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/border-gradients@1.1.0/dist/border-gradients.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fancy-borders@2.0.1/dist/fancy-borders.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/animated-borders@1.0.0/dist/animated-borders.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/border-radius-plus@1.0.2/dist/border-radius-plus.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/btn-animations@1.2.0/dist/btn-anim.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/img-animations@1.0.3/dist/img-anim.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/modal-animations@2.1.0/dist/modal-anim.min.css">
<!-- ===== 代码高亮CSS ===== -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@11.7.0/styles/atom-one-dark.min.css">
<!-- ===== 图标CSS ===== -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/twemoji-colr@1.0.1/twemoji-colr.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/icomoon-icons@1.0.0/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/feather-icons@4.29.0/dist/feather.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/devicons@1.8.0/css/devicons.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<!-- ===== 字体CSS ===== -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-zcool-gdh@1.0.1/css/zcool-gdh.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/text-gradient@1.0.1/dist/text-gradient.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-animate@1.0.0/dist/font-animate.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/symbola-font@1.0.0/css/symbola.min.css">
"""

# ========== 去重后的JS库（约86个）==========
JS_CDN = """
<!-- ===== 工具库JS ===== -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/dayjs@1.11.7/dayjs.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.4/moment.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/axios@1.6.8/dist/axios.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/js-cookie@3.0.5/dist/js.cookie.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/localforage@1.10.0/dist/localforage.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/downloadjs@1.4.7/download.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/resumable.js@1.1.0/resumable.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mime-types@2.1.35/index.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sniffy@2.0.0/dist/sniffy.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/xmldom@0.8.10/lib/xmldom.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/xml-js@1.6.11/dist/xml-js.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/clipboard@2.0.11/dist/clipboard.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/sjcl/1.0.8/sjcl.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/fontfaceobserver@2.3.0/fontfaceobserver.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/linkifyjs@4.1.1/dist/linkify.min.js"></script>
<!-- ===== Vue3全家桶JS ===== -->
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@vueuse/core@10.7.2/dist/index.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/element-plus/dist/index.full.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue3-download@1.0.5/dist/vue3-download.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue3-draggable-resizable@2.0.1/dist/vue3-draggable-resizable.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuedraggable@4.1.0/dist/vuedraggable.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue-flow@1.38.1/dist/vue-flow.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/form-designer-vue3@1.2.0/dist/form-designer-vue3.umd.min.js"></script>
<!-- ===== React/Angular JS ===== -->
<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/@angular/core@16/bundles/core.umd.js"></script>
<!-- ===== CSS框架JS ===== -->
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://unpkg.com/antd/dist/antd.min.js"></script>
<!-- ===== 编辑器JS ===== -->
<script src="https://cdn.quilljs.com/1.3.7/quill.min.js"></script>
<script src="https://unpkg.com/wangeditor@4.7.15/dist/wangEditor.min.js"></script>
<script src="https://cdn.tiny.cloud/1/no-api-key/tinymce/6.8.3/tinymce.min.js"></script>
<!-- ===== 动画/交互JS ===== -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.4/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/animejs@3.2.2/lib/anime.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mo-js@0.288.2/build/mo.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs@2.0.8/hammer.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/interactjs@1.9.19/dist/interact.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/headroom.js@0.12.0/dist/headroom.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
<script src="https://cdn.jsdelivr.net/npm/tsparticles@3.3.0/tsparticles.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lottie-web@5.12.2/build/player/lottie.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/turn.js@4.1.0/build/turn.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/btn-animations@1.2.0/dist/btn-anim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/textillate@0.4.0/jquery.textillate.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/modal-animations@2.1.0/dist/modal-anim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/glow-effects@1.1.0/dist/glow.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/window-animations@1.0.1/dist/window-anim.min.js"></script>
<!-- ===== 图表/可视化JS ===== -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.8/dist/chart.umd.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.157.0/build/three.min.js"></script>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://cdn.jsdelivr.net/npm/leaflet.animatedmarker@0.2.0/dist/leaflet.animatedmarker.min.js"></script>
<!-- ===== 媒体处理JS ===== -->
<script src="https://vjs.zencdn.net/8.6.1/video.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/howler/2.2.3/howler.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.6.1/cropper.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lightgallery.js/1.4.0/js/lightgallery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/canvas2image@1.0.5/canvas2image.min.js"></script>
<!-- ===== 文档处理JS ===== -->
<script src="https://cdn.jsdelivr.net/npm/pdfjs-dist@3.11.174/build/pdf.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mammoth@1.6.0/mammoth.browser.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jspdf@2.5.1/dist/jspdf.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/snap.svg@0.5.1/dist/snap.svg-min.js"></script>
<!-- ===== 代码编辑器/高亮JS ===== -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/prism.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11.8.0/lib/highlight.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/codemirror@5.65.16/lib/codemirror.min.js"></script>
<!-- ===== 表格/弹窗/提示JS ===== -->
<script src="https://cdn.jsdelivr.net/npm/handsontable@13.1.0/dist/handsontable.full.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/masonry-layout@4/dist/masonry.pkgd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/tippy.js@6.3.7/dist/tippy.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/floating-ui@1.6.1/dist/floating-ui.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/simplebar@6.2.5/dist/simplebar.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/nanoscroller@0.8.7/bin/javascripts/jquery.nanoscroller.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/editor-toolbar-kit@1.0.0/dist/toolbar.min.js"></script>
<script src="https://www.jeasyui.com/easyui/jquery.min.js"></script>
<script src="https://www.jeasyui.com/easyui/jquery.easyui.min.js"></script>
<!-- ===== 其他JS ===== -->
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.14.0/dist/tf.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/fullpage.js/dist/fullpage.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.1/build/qrcode.min.js"></script>
<script src="https://res.wx.qq.com/open/js/jweixin-1.6.0.js"></script>
<!-- 注意：jRespond.js和restive为本地路径库，需自行下载引入 -->
"""

# 客服面板HTML
SVC_PANEL = '''
<div class="svc-mask" id="svcMask"></div>
<div class="svc-panel glass-strong" id="svcPanel">
  <div class="panel-inner">
    <div class="panel-title">💬 联系客服 · 资源导航</div>
    <div class="qr-box">
      <div class="qr-frame"><img id="qrImg" src="assets/img/zsm.png" alt="赞赏码" onerror="this.src='assets/img/wxsy1349.png'"></div>
      <div class="qr-name" id="qrName">赞赏二维码</div>
      <button class="qr-switch" id="qrSwitch" type="button">切换到公众号</button>
    </div>
    <p class="qr-tip">欢迎自愿赞赏支持作者</p>
    <div class="wx-id" title="鼠标移过自动复制">
      <span class="wx-label">微信公众号</span>
      <span class="wx-line">wxsy1349</span>
    </div>
    <div class="svc-links">
      <a class="svc-link c1" href="https://app.kwaixiaodian.com/page/kwaishop-store-c-frame-h5/frame?layoutType=4&hyId=kwaishop-store-c-frame-h5&sellerId=1865090819&authorId=1865090819&carrierType=29&carrierId=fva0b4kfnGw&entrance=xdhtlj" target="_blank">🛒 快手小店</a>
      <a class="svc-link c2" href="https://pd.qq.com/s/24yp7y38f" target="_blank">💬 腾讯频道</a>
      <a class="svc-link c3" href="https://www.zhihu.com/people/z6391" target="_blank">💡 知乎</a>
      <a class="svc-link c4" href="https://qm.qq.com/q/VHeRTTdQcu" target="_blank">👥 QQ群</a>
      <a class="svc-link c5" href="https://bolt.cello.so/lsypink3QTR" target="_blank">⚡ 在线编程</a>
      <a class="svc-link c6" href="https://api.u-claw.org/register?aff=9OLG" target="_blank">🦞 OpenClaw</a>
      <a class="svc-link c7" href="https://weibo.com/zdzqxt" target="_blank">📢 微博</a>
      <a class="svc-link c8" href="https://txc.qq.com/embed/367382/new-post/" target="_blank">✍️ 欢迎留言</a>
    </div>
  </div>
</div>
'''

# 悬浮按钮HTML（32x32，客服在上返回顶部在下，贴右侧）
FLOAT_BTNS = '''
<div class="float-btns">
  <button class="fab svc-fab" id="svcToggle" title="联系客服">💬</button>
  <button class="fab back-top" id="backTop" title="返回顶部">🚀</button>
</div>
'''

def render_steps(steps):
    h = '<div class="steps">'
    for i, (title, txt) in enumerate(steps, 1):
        h += f'<div class="step"><div class="step-no">{i}</div><div class="step-body"><h4>{title}</h4><div class="step-txt">{txt}</div></div></div>'
    h += '</div>'
    return h

def code_block(code, lang="python"):
    return f'<div class="code-wrap"><div class="code-bar"><span>{lang}</span><button class="copy-btn" onclick="copyCode(this)">复制</button></div><pre><code>{code}</code></pre></div>'

def gen_ai_page(ai):
    cat = ai.get("cat", "其他")
    slug = ai.get("slug", "unknown")
    name = ai.get("name", "未知")
    ico = ai.get("ico", "🤖")
    tags = ai.get("tags", [])
    brief = ai.get("brief", "")
    links = ai.get("links", [
        ("官网地址", '<a href="#" target="_blank">待补充</a>'),
        ("插件地址", "暂无"),
        ("接口文档", "暂无"),
        ("社群/社区", "暂无"),
        ("微信公众号", "关注AI技术社区"),
        ("微信小程序", "暂无")
    ])
    feat = ai.get("feat", [tags[0] if tags else "AI", "支持API调用", "可内嵌到exe/apk", "持续更新中"])
    intro = ai.get("intro", brief)
    steps = ai.get("steps", [
        ("注册账号", f"访问{name}官网注册账号。"),
        ("获取Key", "在控制台创建应用，获取API Key。"),
        ("配置调用", "使用API Key配置调用参数。"),
        ("测试连接", "发送测试请求验证连接。"),
        ("内嵌部署", "将API调用集成到exe/apk中。")
    ])
    cb_code = ai.get("cb_code", "")

    links_html = ""
    for label, val in links:
        links_html += f'<div class="link-row"><span class="link-label">{label}</span><span class="link-val">{val}</span></div>'

    feat_html = "".join(f'<span class="feat-tag">{f}</span>' for f in feat)

    steps_html = render_steps(steps)
    cb_html = ""
    if cb_code:
        cb_html = f'<h3>🔧 exe/apk内嵌回调函数示例</h3>{code_block(cb_code, "python")}'

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} - AI配置教程</title>
{CSS_CDN}
<link rel="stylesheet" href="../assets/css/main.css">
</head>
<body>
<div class="page">
  <header class="top-bar">
    <a href="../index.html" class="back-btn">← 返回目录</a>
    <h1>{ico} {name}</h1>
    <span class="cat-badge">{cat}</span>
  </header>
  <div class="ai-container">
    <section class="ai-intro glass">
      <h2>📋 简介</h2>
      <p>{intro}</p>
      <div class="feat-tags">{feat_html}</div>
    </section>
    <section class="ai-links glass">
      <h2>🔗 相关渠道</h2>
      {links_html}
    </section>
    <section class="ai-steps glass">
      <h2>📖 部署教程</h2>
      {steps_html}
    </section>
    {cb_html}
  </div>
  <footer class="footer">全国中文AI大全 · {name} · <a href="../index.html">返回目录</a></footer>
</div>
{FLOAT_BTNS}
{SVC_PANEL}
{JS_CDN}
<script src="../assets/js/main.js"></script>
</body>
</html>'''
    return html

# ========== AI数据（含新链接）==========
AIS = [
    {
        "cat": "离线免费", "slug": "ollama", "name": "Ollama", "ico": "🦙",
        "tags": ["离线", "免费", "本地部署"],
        "brief": "一键本地运行大模型，支持LLaMA/Qwen/DeepSeek等",
        "feat": ["完全离线", "免费开源", "一行命令运行", "支持GPU加速"],
        "intro": "Ollama是最流行的本地大模型运行工具，一行命令即可在Windows/Mac/Linux上运行LLaMA、Qwen、DeepSeek、Mistral等开源模型。支持API调用，可内嵌到exe/apk。",
        "links": [
            ("官网地址", '<a href="https://ollama.com" target="_blank">https://ollama.com</a>'),
            ("下载地址", '<a href="https://ollama.com/download" target="_blank">Download</a>'),
            ("模型库", '<a href="https://ollama.com/library" target="_blank">Library</a>'),
            ("接口文档", '<a href="https://github.com/ollama/ollama/blob/main/docs/api.md" target="_blank">API Docs</a>'),
            ("GitHub", '<a href="https://github.com/ollama/ollama" target="_blank">GitHub</a>'),
            ("微信公众号", "关注AI技术社区")
        ],
        "steps": [
            ("下载安装", "访问ollama.com下载对应系统安装包，双击安装。"),
            ("拉取模型", "命令行执行 ollama pull qwen2.5:7b 下载模型。"),
            ("运行对话", "执行 ollama run qwen2.5:7b 开始对话。"),
            ("API调用", "默认监听 http://localhost:11434/api/generate，直接POST请求即可。"),
            ("exe内嵌", "在exe中启动ollama serve，然后HTTP调用API。")
        ],
        "cb_code": '''import requests

def call_ollama(prompt, model="qwen2.5:7b"):
    """内嵌到exe中的Ollama回调函数"""
    resp = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    )
    return resp.json()["response"]

# apk中用OkHttp同理
# OkHttpClient client = new OkHttpClient();
# RequestBody body = RequestBody.create(json, MediaType.parse("application/json"));
# Request request = new Request.Builder().url("http://10.0.2.2:11434/api/generate").post(body).build();'''
    },
    {
        "cat": "离线免费", "slug": "lmstudio", "name": "LM Studio", "ico": "🖥️",
        "tags": ["离线", "免费", "图形界面"],
        "brief": "图形界面本地运行大模型，无需命令行",
        "feat": ["图形界面", "完全离线", "内置API服务器", "支持模型搜索"],
        "intro": "LM Studio提供图形界面管理本地大模型，内置OpenAI兼容API服务器，支持一键下载模型。适合不想用命令行的用户。",
        "links": [
            ("官网地址", '<a href="https://lmstudio.ai" target="_blank">https://lmstudio.ai</a>'),
            ("下载地址", '<a href="https://lmstudio.ai/download" target="_blank">Download</a>'),
            ("模型库", '<a href="https://huggingface.co/models" target="_blank">HuggingFace</a>'),
            ("微信公众号", "关注AI技术社区")
        ],
        "steps": [
            ("下载安装", "访问lmstudio.ai下载安装包。"),
            ("搜索模型", "在搜索栏输入模型名，下载GGUF格式模型。"),
            ("加载模型", "点击模型右侧Load按钮加载。"),
            ("开启API", "在Developer页签开启Local Server，默认端口1234。"),
            ("调用API", "兼容OpenAI格式：http://localhost:1234/v1/chat/completions")
        ]
    },
]

# 其他AI精简版（含新链接）
MORE_AIS = [
    # (分类, slug, 名称, 图标, 标签, 简介, 官网链接)
    ("对话型", "chatgpt", "ChatGPT", "🟢", "OpenAI", "OpenAI官方对话AI", "https://chat.openai.com"),
    ("对话型", "claude", "Claude", "🟣", "Anthropic", "Anthropic对话AI", "https://claude.ai"),
    ("对话型", "gemini", "Gemini", "🔵", "Google", "谷歌多模态AI", "https://gemini.google.com"),
    ("对话型", "doubao", "豆包", "🎵", "字节跳动", "字节跳动对话AI", "https://www.doubao.com"),
    ("对话型", "kimi", "Kimi", "🌙", "月之暗面", "长文本对话AI", "https://kimi.moonshot.cn"),
    ("对话型", "tongyi", "通义千问", "💠", "阿里", "阿里通义千问", "https://www.tongyi.com"),
    ("对话型", "wenxin", "文心一言", "🔴", "百度", "百度文心一言", "https://yiyan.baidu.com"),
    ("对话型", "hunyuan", "混元", "🌀", "腾讯", "腾讯混元大模型", "https://hunyuan.tencent.com"),
    ("对话型", "xinghuo", "星火", "✨", "讯飞", "讯飞星火大模型", "https://xinghuo.xfyun.cn"),
    ("对话型", "deepseek", "DeepSeek", "🐋", "深度求索", "深度求索推理模型", "https://chat.deepseek.com"),
    ("对话型", "zhipu", "智谱清言", "🧠", "智谱AI", "智谱GLM对话", "https://chatglm.cn"),
    ("对话型", "baichuan", "百川", "🏔️", "百川智能", "百川对话模型", "https://www.baichuan-ai.com"),
    ("对话型", "minimax", "MiniMax", "💎", "MiniMax", "海螺AI对话", "https://www.minimaxi.com"),
    # API类
    ("API类", "openai", "OpenAI API", "🟢", "API", "GPT系列API", "https://platform.openai.com"),
    ("API类", "anthropic", "Claude API", "🟣", "API", "Claude系列API", "https://console.anthropic.com"),
    ("API类", "deepseek-api", "DeepSeek API", "🐋", "API", "DeepSeek API", "https://platform.deepseek.com"),
    ("API类", "moonshot-api", "Moonshot API", "🌙", "API", "Kimi开放平台", "https://platform.moonshot.cn"),
    ("API类", "zhipu-api", "智谱API", "🧠", "API", "智谱开放平台", "https://open.bigmodel.cn"),
    ("API类", "baichuan-api", "百川API", "🏔️", "API", "百川开放平台", "https://platform.baichuan-ai.com"),
    ("API类", "minimax-api", "MiniMax API", "💎", "API", "MiniMax开放平台", "https://api.minimaxi.com"),
    ("API类", "dashscope", "通义API", "💠", "API", "阿里百炼平台", "https://dashscope.aliyun.com"),
    ("API类", "azure", "Azure OpenAI", "☁️", "API", "微软Azure OpenAI", "https://azure.microsoft.com"),
    ("API类", "openrouter", "OpenRouter", "🔀", "API", "多模型聚合API", "https://openrouter.ai"),
    ("API类", "siliconflow", "硅基流动", "🔬", "API", "硅基流动API", "https://siliconflow.cn"),
    ("API类", "stepfun", "阶跃Step", "📈", "API", "阶跃星辰", "https://platform.stepfun.com/?invite_code=SBITYKKU"),
    ("API类", "skylark", "面壁智能", "🧊", "API", "面壁智能API", "https://www.modelbest.cn"),
    # Agent类
    ("Agent类", "coze", "Coze", "🤖", "字节", "扣子智能体平台", "https://www.coze.cn"),
    ("Agent类", "dify", "Dify", "🔧", "开源", "开源LLM应用开发平台", "https://dify.ai"),
    ("Agent类", "fastgpt", "FastGPT", "⚡", "开源", "知识库问答系统", "https://fastgpt.io"),
    ("Agent类", "n8n", "n8n", "🔗", "自动化", "工作流自动化", "https://n8n.io"),
    ("Agent类", "zapier", "Zapier", "⚡", "自动化", "应用集成自动化", "https://zapier.com"),
    ("Agent类", "ifttt", "IFTTT", "🔔", "自动化", "如果这样就那样", "https://ifttt.com"),
    ("Agent类", "make", "Make", "🎭", "自动化", "可视化自动化", "https://www.make.com"),
    ("Agent类", "powerautomate", "Power Automate", "⚙️", "微软", "微软自动化", "https://make.powerautomate.com"),
    ("Agent类", "autogen", "AutoGen", "🤖", "微软", "多Agent对话框架", "https://microsoft.github.io/autogen"),
    ("Agent类", "crewai", "CrewAI", "👥", "Agent", "多Agent协作框架", "https://www.crewai.com"),
    ("Agent类", "langchain", "LangChain", "⛓️", "框架", "LLM应用开发框架", "https://www.langchain.com"),
    ("Agent类", "githubcopilot", "GitHub Copilot", "🐱", "编程", "AI编程助手", "https://github.com/features/copilot"),
    # RPA类
    ("RPA类", "yingdao", "影刀RPA", "🦾", "RPA", "影刀RPA", "https://www.winrobot360.com/share/activity?inviteUserUuid=991689363336437760"),
    ("RPA类", "shizai", "实在智能Agent", "🎯", "RPA", "实在智能RPA", "https://www.ai-indeed.com/products/agentRpa?pik=B4F4620"),
    ("RPA类", "uibot", "UiBot", "🤖", "RPA", "UiBot RPA", "https://www.uibot.com.cn"),
    ("RPA类", "uipath", "UiPath", "🖱️", "RPA", "全球RPA领导者", "https://www.uipath.com"),
    ("RPA类", "automationanywhere", "Automation Anywhere", "🤖", "RPA", "企业级RPA", "https://www.automationanywhere.com"),
    ("RPA类", "workbuddy", "腾讯workbuddy", "💼", "腾讯", "腾讯智能工作助手", "https://www.workbuddy.cn/events/invite?inviteCode=xiiy268mivibykb"),
    # 生产类
    ("生产类", "aipy", "爱派Aipy", "💝", "AI工具", "爱派AI工具集", "https://promo.aipyaipy.com/?referral=aipy_Aazb"),
    ("生产类", "pixverse", "PixVerse", "🎬", "视频", "AI视频生成器", "https://share.pai.video/referral/MSLACW85"),
    ("生产类", "runway", "Runway", "🎥", "视频", "AI视频编辑", "https://runwayml.com"),
    ("生产类", "miaoda", "秒哒", "⚡", "全能", "秒哒全能AI", "https://www.miaoda.cn/?invitecode=user-79m6k4scy9du"),
    ("生产类", "feitui", "沸推AI", "🔥", "推广", "沸推AI推广", "https://motubizhi.com/?inviteCode=989700"),
    ("生产类", "feiying", "飞影数字人", "🧑", "数字人", "飞影AI数字人", "https://hifly.cc/i/rDdw27xDZ0s"),
    ("生产类", "liblib", "LiblibAI", "🎨", "生图", "在线生图平台", "https://www.liblib.art/viphome?referralCode=6kEkNhMV"),
    ("生产类", "canva", "Canva", "🎨", "设计", "AI设计平台", "https://www.canva.com"),
    ("生产类", "gamma", "Gamma", "📊", "PPT", "AI生成PPT", "https://gamma.app"),
    ("生产类", "capcut", "剪映", "✂️", "视频", "AI视频剪辑", "https://www.capcut.cn"),
    ("生产类", "wenxin-vegan", "文心素食助手", "🥗", "智能体", "文心素食助手智能体", "https://mbd.baidu.com/ma/s/Z6liMqPw"),
    ("生产类", "typefun", "AI打字学习", "⌨️", "学习", "AI助力快速学会打字", "https://www.type.fun/share?c=885264312220844032"),
    ("生产类", "notionai", "Notion AI", "📝", "写作", "Notion内置AI", "https://www.notion.so/product/ai"),
    ("生产类", "openclaw", "OpenClaw虾盘云", "🦞", "AI助手", "虾盘云AI助手", "https://api.u-claw.org/register?aff=9OLG"),
    ("生产类", "bianjie", "边界AI", "🌐", "AI助手", "边界AI电脑版", "https://yyai8.com/download?invite_code=868A92"),
    # 编程类
    ("编程类", "cursor", "Cursor", "✏️", "编程", "AI代码编辑器", "https://cursor.sh"),
    ("编程类", "trae", "Trae", "🚀", "编程", "字节AI编程", "https://www.trae.ai"),
    ("编程类", "codegeex", "CodeGeeX", "💻", "编程", "智谱AI编程", "https://codegeex.cn"),
    ("编程类", "codeium", "Codeium", "🔮", "编程", "AI代码补全", "https://codeium.com"),
    ("编程类", "tongyi-lingma", "通义灵码", "🐎", "编程", "阿里AI编程", "https://lingma.aliyun.com"),
    ("编程类", "bolt", "Bolt在线编程", "⚡", "编程", "在线AI编程助手", "https://bolt.cello.so/lsypink3QTR"),
    ("编程类", "360gpt", "360智脑", "🔵", "对话", "360智脑", "https://chat.360.com"),
    # 离线更多
    ("离线免费", "gpt4all", "GPT4All", "📦", "离线", "本地AI对话", "https://gpt4all.io"),
    ("离线免费", "text-generation-webui", "Oobabooga", "🕸️", "离线", "文本生成WebUI", "https://github.com/oobabooga/text-generation-webui"),
    ("离线免费", "koboldcpp", "KoboldCpp", "🐉", "离线", "KoboldAI CPP", "https://github.com/LostRuins/koboldcpp"),
    ("离线免费", "llama-cpp", "llama.cpp", "🦙", "离线", "GGUF模型推理", "https://github.com/ggerganov/llama.cpp"),
    ("离线免费", "vllm", "vLLM", "⚡", "离线", "高吞吐推理", "https://github.com/vllm-project/vllm"),
    ("离线免费", "xinference", "Xinference", "🎈", "离线", "模型推理平台", "https://github.com/xorbitsai/inference"),
    ("离线免费", "anything-llm", "AnythingLLM", "📄", "离线", "文档AI对话", "https://anythingllm.com"),
]

def gen_index():
    # 分类统计
    cats = {}
    for ai in AIS:
        c = ai.get("cat", "其他")
        cats.setdefault(c, []).append(ai)
    for item in MORE_AIS:
        c = item[0]
        cats.setdefault(c, []).append({
            "cat": c, "slug": item[1], "name": item[2], "ico": item[3],
            "tags": [item[4]], "brief": item[5]
        })

    # 分类顺序
    cat_order = ["离线免费", "对话型", "API类", "Agent类", "RPA类", "生产类", "编程类"]
    cat_icons = {
        "离线免费": "💻", "对话型": "💬", "API类": "🔑",
        "Agent类": "🤖", "RPA类": "🦾", "生产类": "🎨", "编程类": "💻"
    }

    sections = ""
    for cat in cat_order:
        if cat not in cats:
            continue
        ais = cats[cat]
        cards = ""
        for ai in ais:
            slug = ai["slug"]
            # 检查是完整版还是精简版
            if ai in AIS:
                link = f"pages/{slug}.html"
            else:
                link = f"pages/{slug}.html"
            cards += f'''<a class="card glass" href="{link}">
  <div class="card-ico">{ai.get("ico","🤖")}</div>
  <h3>{ai["name"]}</h3>
  <p>{ai.get("brief","")}</p>
  <div class="card-arrow">›</div>
</a>'''
        sections += f'''<section class="cat-section">
  <h2 class="cat-title">{cat_icons.get(cat,"📁")} {cat} <span class="cat-count">{len(ais)}</span></h2>
  <div class="card-grid">{cards}</div>
</section>'''

    total = sum(len(v) for v in cats.values())

    cdn_init_js = """
<script>
// ===== CDN库交互初始化（详细中文注释）=====
// AOS滚动动画初始化
if(typeof AOS!=="undefined"){AOS.init({duration:800,once:true});}
// GSAP动画：标题入场
if(typeof gsap!=="undefined"){gsap.from(".hero-title",{y:-30,opacity:0,duration:1});}
// 代码高亮
if(typeof hljs!=="undefined"){document.querySelectorAll("pre code").forEach(function(e){hljs.highlightElement(e);});}
if(typeof Prism!=="undefined"){Prism.highlightAll();}
// Simplebar滚动条增强
if(typeof Simplebar!=="undefined"){document.querySelectorAll(".card-grid").forEach(function(e){new Simplebar(e);});}
// Tippy提示
if(typeof tippy!=="undefined"){tippy(".fab",{theme:"glass"});}
// 回到顶部头部隐藏
if(typeof Headroom!=="undefined"){var hd=document.querySelector(".top-bar");if(hd){new Headroom(hd).init();}}
</script>
"""

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全国中文AI大全 - 智能目录</title>
{CSS_CDN}
<link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
<div class="page">
  <header class="hero glass">
    <h1 class="hero-title">🌟 全国中文AI大全</h1>
    <p class="hero-sub">{total}个AI智能体 · 离线/联网/API/Agent/RPA/生产/编程 全分类</p>
    <div class="search-area">
      <div class="search-box glass-strong">
        <input type="text" id="searchInput" placeholder="🔍 搜索AI名称，或粘贴B站链接，或输入关键词全网搜索..." autocomplete="off">
        <button class="search-btn" id="searchBtn">搜索</button>
      </div>
      <div class="search-modes">
        <button class="mode-btn active" data-mode="local">📂 站内搜索</button>
        <button class="mode-btn" data-mode="web">🌐 全网聚合搜索</button>
      </div>
    </div>
    <div id="searchResults" class="search-results" style="display:none"></div>
    <div id="biliResult" class="bili-result" style="display:none"></div>
  </header>
  <main class="main-content">
    {sections}
  </main>
  <footer class="footer glass">
    <p>全国中文AI大全 · {total}个AI · 金色玻璃水晶质感 · 万能聚合搜索</p>
    <p>微信公众号：wxsy1349 · 欢迎自愿赞赏支持作者</p>
  </footer>
</div>
{FLOAT_BTNS}
{SVC_PANEL}
{JS_CDN}
{cdn_init_js}
<script src="assets/js/main.js"></script>
</body>
</html>'''
    return html

def main():
    pages_dir = os.path.join(BASE, "pages")
    os.makedirs(pages_dir, exist_ok=True)

    # 生成完整版AI单页
    count = 0
    for ai in AIS:
        html = gen_ai_page(ai)
        path = os.path.join(pages_dir, f"{ai['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1

    # 生成精简版AI单页
    for item in MORE_AIS:
        cat, slug, name, ico, tag, brief, url = item
        ai = {
            "cat": cat, "slug": slug, "name": name, "ico": ico,
            "tags": [tag], "brief": brief,
            "links": [("官网地址", f'<a href="{url}" target="_blank">{url}</a>'), ("微信公众号", "wxsy1349")]
        }
        html = gen_ai_page(ai)
        path = os.path.join(pages_dir, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1

    # MCP单页
    mcp_html = gen_ai_page({
        "cat": "Agent类", "slug": "mcp", "name": "MCP协议本地部署", "ico": "🔌",
        "tags": ["MCP", "协议", "本地部署"], "brief": "Model Context Protocol本地部署教程",
        "feat": ["开源协议", "本地运行", "工具调用", "AI连接外部工具"],
        "intro": "MCP（Model Context Protocol）是Anthropic推出的开放协议，让AI连接外部工具和数据源。本地部署后可实现文件读写、数据库查询、浏览器控制等能力。",
        "links": [
            ("官网地址", '<a href="https://modelcontextprotocol.io" target="_blank">modelcontextprotocol.io</a>'),
            ("GitHub", '<a href="https://github.com/modelcontextprotocol" target="_blank">GitHub</a>'),
            ("规范文档", '<a href="https://spec.modelcontextprotocol.io" target="_blank">Specification</a>')
        ],
        "steps": [
            ("安装Python", "安装Python 3.10+，确保pip可用。"),
            ("安装MCP SDK", "执行 pip install mcp 安装SDK。"),
            ("编写服务端", "创建server.py，定义tools和resources。"),
            ("运行服务", "执行 python server.py，MCP通过stdio通信。"),
            ("客户端连接", "在支持MCP的客户端（如Claude Desktop）中配置。")
        ],
        "cb_code": '''from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """加法工具"""
    return a + b
if __name__ == "__main__":
    mcp.run(transport="stdio")'''
    })
    with open(os.path.join(pages_dir, "mcp.html"), "w", encoding="utf-8") as f:
        f.write(mcp_html)
    count += 1

    # 首页
    idx = gen_index()
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx)

    print(f"✅ 生成 {count} 个AI单页 + 首页")

if __name__ == "__main__":
    main()
