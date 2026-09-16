/* ============================================================
   AI大全全站交互脚本 v2.0
   客服面板(默认隐藏/点击弹出/内外关闭/1px滚动条)
   悬浮按钮(32x32/客服在上返回顶部在下/贴右侧/滚动隐藏)
   聚合搜索(10+引擎iframe页面内展示/不跳转外部)
   B站视频解析(站内播放/复制链接)
   代码块复制按钮
   ============================================================ */
(function(){
"use strict";

/* ===== 工具函数 ===== */
function $(id){return document.getElementById(id);}
function esc(s){var d=document.createElement("div");d.textContent=s;return d.innerHTML;}
function copyText(text){
  if(navigator.clipboard&&window.isSecureContext){
    navigator.clipboard.writeText(text).catch(function(){fb(text);});
  }else{fb(text);}
}
function fb(text){
  var ta=document.createElement("textarea");ta.value=text;
  ta.style.cssText="position:fixed;opacity:0;left:-9999px";
  document.body.appendChild(ta);ta.select();
  try{document.execCommand("copy");}catch(e){}
  document.body.removeChild(ta);
}

/* ===== 客服面板 ===== */
var svcToggle=$("svcToggle"),svcPanel=$("svcPanel"),svcMask=$("svcMask"),svcBtn=document.querySelector(".svc-fab");
if(svcToggle&&svcPanel){
  // 点击客服按钮切换面板
  svcToggle.addEventListener("click",function(e){
    e.stopPropagation();
    svcPanel.classList.toggle("open");
    if(svcMask)svcMask.classList.toggle("show");
  });
  // 点击遮罩关闭
  if(svcMask)svcMask.addEventListener("click",function(){
    svcPanel.classList.remove("open");svcMask.classList.remove("show");
  });
  // 点击面板外部关闭
  document.addEventListener("click",function(e){
    if(svcPanel.classList.contains("open")&&!svcPanel.contains(e.target)&&e.target!==svcToggle){
      svcPanel.classList.remove("open");
      if(svcMask)svcMask.classList.remove("show");
    }
  });
  // ESC关闭
  document.addEventListener("keydown",function(e){
    if(e.key==="Escape"&&svcPanel.classList.contains("open")){
      svcPanel.classList.remove("open");
      if(svcMask)svcMask.classList.remove("show");
    }
  });
}

/* ===== 二维码切换 ===== */
var qrSwitch=$("qrSwitch"),qrImg=$("qrImg"),qrName=$("qrName");
if(qrSwitch){
  var showingWx=false;
  qrSwitch.addEventListener("click",function(){
    showingWx=!showingWx;
    if(showingWx){
      qrImg.src="assets/img/wxsy1349.png";qrName.textContent="微信公众号";
      qrSwitch.textContent="切换到赞赏码";
    }else{
      qrImg.src="assets/img/zsm.png";qrName.textContent="赞赏二维码";
      qrSwitch.textContent="切换到公众号";
    }
  });
}

/* ===== 公众号悬停复制 ===== */
var wxLine=document.querySelector(".wx-line");
if(wxLine){
  wxLine.addEventListener("mouseenter",function(){
    copyText("wxsy1349");
    wxLine.style.color="#4caf50";
    wxLine.title="已复制: wxsy1349";
  });
  wxLine.addEventListener("mouseleave",function(){
    wxLine.style.color="";
  });
}

/* ===== 悬浮按钮：滚动隐藏/停止显示 ===== */
var floatBtns=document.querySelector(".float-btns");
var backTop=$("backTop");
if(floatBtns){
  var scrollTimer=null;
  window.addEventListener("scroll",function(){
    floatBtns.classList.add("hide");
    if(scrollTimer)clearTimeout(scrollTimer);
    scrollTimer=setTimeout(function(){
      floatBtns.classList.remove("hide");
    },300);
  });
}
if(backTop){
  backTop.addEventListener("click",function(){
    window.scrollTo({top:0,behavior:"smooth"});
  });
}

/* ===== 代码块复制按钮 ===== */
document.querySelectorAll(".code-wrap").forEach(function(wrap){
  var btn=wrap.querySelector(".copy-btn");
  var pre=wrap.querySelector("pre");
  if(btn&&pre){
    btn.addEventListener("click",function(){
      copyText(pre.textContent);
      btn.textContent="已复制";
      setTimeout(function(){btn.textContent="复制";},1500);
    });
  }
});

/* ============================================================
   万能聚合搜索引擎
   10+引擎全部iframe页面内展示，不跳转外部浏览器
   ============================================================ */
var searchInput=$("searchInput"),searchBtn=$("searchBtn");
var searchResults=$("searchResults"),biliResult=$("biliResult");
var modeBtns=document.querySelectorAll(".mode-btn");
var currentMode="local";

// 搜索引擎配置表（全部iframe页面内展示）
var ENGINES={
  baidu:{name:"百度",url:"https://www.baidu.com/s?wd=",icon:"🔍"},
  google:{name:"谷歌",url:"https://www.google.com/search?q=",icon:"🌐"},
  bing:{name:"必应",url:"https://www.bing.com/search?q=",icon:"🔷"},
  zhihu:{name:"知乎",url:"https://www.zhihu.com/search?q=",icon:"💡"},
  wechat:{name:"微信",url:"https://weixin.sogou.com/weixin?type=2&query=",icon:"💬"},
  weibo:{name:"微博",url:"https://s.weibo.com/weibo/",icon:"📢"},
  douban:{name:"豆瓣",url:"https://www.douban.com/search?q=",icon:"📚"},
  jd:{name:"京东",url:"https://search.jd.com/Search?enc=utf-8&keyword=",icon:"🛒"},
  taobao:{name:"淘宝",url:"https://s.taobao.com/search?q=",icon:"🛍️"},
  music:{name:"音乐",url:"https://music.hao123.com/search?key=",icon:"🎵"},
  pan:{name:"网盘",url:"https://www.panc.cc/s/",icon:"💾"},
  map:{name:"地图",url:"https://ditu.amap.com/search?query=",icon:"🗺️"},
  bilibili:{name:"B站",url:"https://search.bilibili.com/all?keyword=",icon:"📺"}
};

// 模式切换
modeBtns.forEach(function(btn){
  btn.addEventListener("click",function(){
    modeBtns.forEach(function(b){b.classList.remove("active");});
    btn.classList.add("active");
    currentMode=btn.getAttribute("data-mode");
  });
});

// 搜索主入口
if(searchBtn){
  searchBtn.addEventListener("click",doSearch);
}
if(searchInput){
  searchInput.addEventListener("keydown",function(e){
    if(e.key==="Enter")doSearch();
  });
}

function doSearch(){
  var q=searchInput.value.trim();
  if(!q)return;
  // 先检测是否是B站链接
  var video=detectVideo(q);
  if(video){
    biliResolve(q);
    return;
  }
  if(currentMode==="local"){
    localSearch(q);
  }else{
    aggregateSearch(q);
  }
}

/* 站内搜索 */
function localSearch(q){
  var cards=document.querySelectorAll(".card");
  var results=[];
  q=q.toLowerCase();
  cards.forEach(function(card){
    var text=card.textContent.toLowerCase();
    if(text.indexOf(q)>=0){
      results.push(card);
    }
  });
  if(searchResults){
    searchResults.style.display="block";
    if(results.length===0){
      searchResults.innerHTML='<div class="search-empty">站内没有找到相关AI，试试全网聚合搜索</div>';
    }else{
      searchResults.innerHTML='<div class="search-title">站内找到 '+results.length+' 个AI</div><div class="card-grid">';
      results.forEach(function(card){
        searchResults.querySelector(".card-grid").appendChild(card.cloneNode(true));
      });
      searchResults.innerHTML+="</div>";
    }
    searchResults.scrollIntoView({behavior:"smooth"});
  }
}

/* 全网聚合搜索：所有引擎iframe页面内展示 */
function aggregateSearch(q){
  if(!searchResults)return;
  searchResults.style.display="block";
  var engKeys=["baidu","google","bing","zhihu","wechat","weibo","douban","jd","taobao","music","pan","map","bilibili"];
  var html='<div class="agg-container glass-strong">';
  html+='<div class="agg-title">🌐 聚合搜索：'+esc(q)+'</div>';
  html+='<div class="agg-tabs">';
  engKeys.forEach(function(k,i){
    var e=ENGINES[k];
    html+='<button class="agg-tab'+(i===0?" active":"")+'" data-engine="'+k+'">'+e.icon+' '+e.name+'</button>';
  });
  html+='</div>';
  engKeys.forEach(function(k,i){
    html+='<div class="agg-panel" id="agg-'+k+'"'+(i>0?' style="display:none"':'')+'></div>';
  });
  html+='</div>';
  searchResults.innerHTML=html;
  // 默认加载百度
  loadEngineFrame("baidu",q);
  // 标签切换
  searchResults.querySelectorAll(".agg-tab").forEach(function(tab){
    tab.addEventListener("click",function(){
      searchResults.querySelectorAll(".agg-tab").forEach(function(t){t.classList.remove("active");});
      tab.classList.add("active");
      searchResults.querySelectorAll(".agg-panel").forEach(function(p){p.style.display="none";});
      var eng=tab.getAttribute("data-engine");
      var panel=$("agg-"+eng);
      panel.style.display="block";
      // 如果还没加载就加载
      if(!panel.getAttribute("data-loaded")){
        loadEngineFrame(eng,q);
      }
    });
  });
  searchResults.scrollIntoView({behavior:"smooth"});
}

function loadEngineFrame(eng,q){
  var panel=$("agg-"+eng);
  if(!panel)return;
  panel.innerHTML='<div class="agg-loading">加载'+ENGINES[eng].name+'搜索结果...</div>';
  var url=ENGINES[eng].url+encodeURIComponent(q);
  var iframe=document.createElement("iframe");
  iframe.src=url;
  iframe.className="agg-iframe";
  iframe.setAttribute("allowfullscreen","");
  iframe.onload=function(){
    panel.innerHTML="";
    panel.appendChild(iframe);
  };
  // 超时兜底
  setTimeout(function(){
    if(!panel.querySelector("iframe")){
      panel.innerHTML='<div class="agg-loading">加载中...<br><a href="'+url+'" target="_blank">新窗口打开'+ENGINES[eng].name+'</a></div>';
    }
  },8000);
  panel.setAttribute("data-loaded","1");
}

/* ===== B站视频识别与解析 ===== */
function detectVideo(input){
  var t=(input||"").trim();
  if(/bilibili\.com|b23\.tv|BV[0-9A-Za-z]{10}|av\d+/i.test(t))return{platform:"bilibili",url:t};
  return null;
}

function biliResolve(input){
  if(!biliResult)return;
  biliResult.style.display="block";
  biliResult.innerHTML='<div class="agg-loading">正在解析B站视频...</div>';
  var bv=input.match(/BV[0-9A-Za-z]{10}/i);
  var av=input.match(/av(\d+)/i);
  var apiUrl="https://api.bilibili.com/x/web-interface/view?";
  if(bv)apiUrl+="bvid="+encodeURIComponent(bv[0]);
  else if(av)apiUrl+="aid="+av[1];
  else{
    // 直接搜索
    biliSearch(input);
    return;
  }
  fetch(apiUrl,{headers:{"Referer":"https://www.bilibili.com/"}})
    .then(function(r){return r.json();})
    .then(function(d){
      if(d.code!==0||!d.data){
        biliResult.innerHTML='<div class="agg-loading">解析失败，尝试搜索...</div>';
        biliSearch(input);
        return;
      }
      renderBili(d.data);
    })
    .catch(function(){
      biliResult.innerHTML='<div class="agg-loading">网络错误，尝试搜索...</div>';
      biliSearch(input);
    });
}

function renderBili(d){
  var bvid=d.bvid,cid=d.cid;
  var videoUrl="https://www.bilibili.com/video/"+bvid;
  var h='<div class="bili-card glass-strong">';
  h+='<h3 class="bili-title">'+esc(d.title||"")+'</h3>';
  h+='<div class="bili-player"><iframe src="https://player.bilibili.com/player.html?bvid='+bvid+'&cid='+cid+'&autoplay=0" allowfullscreen></iframe>';
  h+='<button class="bili-copy-btn">📋 复制视频链接</button></div>';
  h+='<div class="bili-meta">UP: '+esc(d.owner&&d.owner.name||"")+' · 播放: '+(d.stat&&d.stat.view||0)+' · 点赞: '+(d.stat&&d.stat.like||0)+'</div>';
  h+='</div>';
  biliResult.innerHTML=h;
  var btn=biliResult.querySelector(".bili-copy-btn");
  if(btn){
    btn.addEventListener("click",function(){
      copyText(videoUrl);
      btn.textContent="✅ 已复制";
      setTimeout(function(){btn.textContent="📋 复制视频链接";},1500);
    });
  }
  biliResult.scrollIntoView({behavior:"smooth"});
}

function biliSearch(kw){
  fetch("https://api.bilibili.com/x/web-interface/search/all/v2?keyword="+encodeURIComponent(kw)+"&page=1",{
    headers:{"Referer":"https://www.bilibili.com/"}
  })
    .then(function(r){return r.json();})
    .then(function(d){
      var results=[];
      if(d.data&&d.data.result){
        d.data.result.forEach(function(r){
          if(r.result_type==="video"&&r.data)results=results.concat(r.data);
        });
      }
      if(!results.length){
        biliResult.innerHTML='<div class="agg-loading">B站搜索无结果</div>';
        return;
      }
      var h='<div class="bili-search-list">';
      h+='<div class="agg-title">📺 B站搜索结果</div>';
      results.slice(0,8).forEach(function(v){
        h+='<div class="bili-item" data-bvid="'+(v.bvid||"")+'">';
        h+='<h4>'+esc((v.title||"").replace(/<[^>]+>/g,""))+'</h4>';
        h+='<p>UP: '+esc(v.author||"")+' · 播放: '+(v.play||0)+'</p>';
        h+='<button class="bili-play-btn">▶ 播放</button></div>';
      });
      h+='</div>';
      biliResult.innerHTML=h;
      biliResult.querySelectorAll(".bili-item").forEach(function(item){
        item.addEventListener("click",function(){
          biliResolve(item.getAttribute("data-bvid"));
        });
      });
    })
    .catch(function(){
      biliResult.innerHTML='<div class="agg-loading">B站搜索失败</div>';
    });
}

})();
