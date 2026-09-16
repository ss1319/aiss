/* ============================================================
 * Universal Search Engine SDK
 * Version: 2.0.0
 * 15 engines + video auto-detect + inline player + aggregate search
 * All paths via UniversalSearch.config variables
 * ============================================================ */
(function (global) {
  "use strict";

  var CONFIG = {
    containers: { input: "ss-input", engine: "ss-engine", button: "ss-go", results: "ss-results", player: "ss-player" },
    engines: {
      baidu: "https://www.baidu.com/s?wd=", google: "https://www.google.com/search?q=",
      bing: "https://www.bing.com/search?q=", sogou: "https://www.sogou.com/web?query=",
      so360: "https://www.so.com/s?q=", toutiao: "https://so.toutiao.com/search?keyword=",
      wechat: "https://weixin.sogou.com/weixin?type=2&query=", zhihu: "https://www.zhihu.com/search?type=content&q=",
      bilibili: "https://search.bilibili.com/all?keyword=", douyin: "https://www.douyin.com/search/",
      kuaishou: "https://www.kuaishou.com/search/video?searchKey=", youku: "https://so.youku.com/search_video/q_",
      iqiyi: "https://so.iqiyi.com/so/q_", tencentvideo: "https://v.qq.com/x/search/?q=", xigua: "https://www.ixigua.com/search/"
    },
    api: {
      biliView: "https://api.bilibili.com/x/web-interface/view?",
      biliSearch: "https://api.bilibili.com/x/web-interface/search/all/v2?",
      biliPlayer: "https://player.bilibili.com/player.html?",
      music163: "https://music.163.com/#/search/m/?s=",
      qqMusic: "https://y.qq.com/n/ryqq/search?w=",
      kugou: "https://www.kugou.com/yy/html/search.html#searchType=song&searchKey="
    },
    aiBackend: null,
    callbacks: { onVideoPlay: null, onMusicPlay: null, onArticleOpen: null, onAiResult: null, onError: null }
  };

  function $(id) { return document.getElementById(id); }
  function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }
  function copyText(text) {
    try { if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).catch(function(){fb(text)}); else fb(text); } catch(e) { fb(text); }
  }
  function fb(text) { var ta=document.createElement("textarea"); ta.value=text; ta.style.cssText="position:fixed;opacity:0;left:-9999px"; document.body.appendChild(ta); ta.select(); try{document.execCommand("copy")}catch(e){} document.body.removeChild(ta); }

  function detectVideo(input) {
    var t=(input||"").trim();
    if(/bilibili\.com|b23\.tv|BV[0-9A-Za-z]{10}|av\d+/i.test(t)) return {platform:"bilibili",url:t};
    if(/douyin\.com|iesdouyin\.com|v\.douyin/i.test(t)) return {platform:"douyin",url:t};
    if(/kuaishou\.com|gifshow\.com/i.test(t)) return {platform:"kuaishou",url:t};
    if(/youku\.com|v\.youku/i.test(t)) return {platform:"youku",url:t};
    if(/v\.qq\.com/i.test(t)) return {platform:"tencentvideo",url:t};
    if(/iqiyi\.com/i.test(t)) return {platform:"iqiyi",url:t};
    if(/ixigua\.com|xigua/i.test(t)) return {platform:"xigua",url:t};
    return null;
  }

  function biliResolve(input, area) {
    if(!area) area=$(CONFIG.containers.player)||document.createElement("div");
    area.style.display="block"; area.innerHTML='<div class="ss-loading">Loading...</div>';
    var bv=input.match(/BV[0-9A-Za-z]{10}/i),av=input.match(/av(\d+)/i),aid=input.match(/^(\d+)$/);
    var url=CONFIG.api.biliView;
    if(bv) url+="bvid="+encodeURIComponent(bv[0]); else if(av) url+="aid="+av[1]; else if(aid) url+="aid="+aid[1];
    else { biliSearch(input, area); return; }
    fetch(url,{headers:{"Referer":"https://www.bilibili.com/"}}).then(function(r){return r.json()}).then(function(d){
      if(d.code!==0||!d.data){area.innerHTML='<div class="ss-error">Error</div>';return;}
      renderBili(d.data, area);
    }).catch(function(){area.innerHTML='<div class="ss-error">Request failed</div>';});
  }

  function renderBili(d, area) {
    var bvid=d.bvid,cid=d.cid,videoUrl="https://www.bilibili.com/video/"+bvid;
    var h='<div class="ss-video-card"><h3 class="ss-video-title">'+esc(d.title||"")+'</h3>';
    h+='<div class="ss-video-frame"><iframe src="'+CONFIG.api.biliPlayer+'bvid='+bvid+'&cid='+cid+'&autoplay=0" allowfullscreen></iframe>';
    h+='<button class="ss-copy-btn">Copy Link</button></div></div>';
    area.innerHTML=h;
    var btn=area.querySelector(".ss-copy-btn");
    if(btn) btn.addEventListener("click",function(){copyText(videoUrl);btn.textContent="Copied!";setTimeout(function(){btn.textContent="Copy Link";},1500);});
    if(CONFIG.callbacks.onVideoPlay) CONFIG.callbacks.onVideoPlay({bvid:bvid,title:d.title,url:videoUrl});
    area.scrollIntoView({behavior:"smooth",block:"start"});
  }

  function biliSearch(kw, area) {
    fetch(CONFIG.api.biliSearch+"keyword="+encodeURIComponent(kw)+"&page=1",{headers:{"Referer":"https://www.bilibili.com/"}})
      .then(function(r){return r.json()}).then(function(d){
        var results=[]; (d.data&&d.data.result||[]).forEach(function(r){if(r.result_type==="video"&&r.data)results=results.concat(r.data);});
        if(!results.length){area.innerHTML='<div class="ss-empty">No results</div>';return;}
        var grid='<div class="ss-video-grid">';
        results.slice(0,8).forEach(function(v){
          grid+='<div class="ss-video-item" data-bvid="'+(v.bvid||"")+'"><h4>'+esc((v.title||"").replace(/<[^>]+>/g,""))+'</h4><p>UP: '+esc(v.author||"")+'</p><button class="ss-play-btn">Play</button></div>';
        });
        grid+='</div>'; area.innerHTML=grid;
        area.querySelectorAll("[data-bvid]").forEach(function(c){c.addEventListener("click",function(){biliResolve(c.getAttribute("data-bvid"),area);});});
      }).catch(function(){area.innerHTML='<div class="ss-error">Search failed</div>';});
  }

  function aggregateSearch(kw, area) {
    if(!area) area=$(CONFIG.containers.results)||document.createElement("div");
    area.style.display="block";
    var h='<div class="ss-aggregate"><h3 class="ss-agg-title">Results: '+esc(kw)+'</h3><div class="ss-tabs">';
    ["video","music","article","web","ai"].forEach(function(t,i){
      h+='<button class="ss-tab'+(i===0?" active":"")+'" data-tab="'+t+'">'+(t==="video"?"Video":t==="music"?"Music":t==="article"?"Article":t==="web"?"Web":"AI")+'</button>';
    });
    h+='</div>';
    ["video","music","article","web","ai"].forEach(function(t,i){h+='<div class="ss-panel" id="ss-panel-'+t+'"'+(i>0?' style="display:none"':'')+'></div>';});
    h+='</div>'; area.innerHTML=h;
    area.querySelectorAll(".ss-tab").forEach(function(t){
      t.addEventListener("click",function(){
        area.querySelectorAll(".ss-tab").forEach(function(x){x.classList.remove("active")}); t.classList.add("active");
        area.querySelectorAll(".ss-panel").forEach(function(p){p.style.display="none"});
        $("ss-panel-"+t.getAttribute("data-tab")).style.display="block";
      });
    });
    // Video
    var vArea=$("ss-panel-video"); vArea.innerHTML='<div class="ss-loading">Loading...</div>';
    fetch(CONFIG.api.biliSearch+"keyword="+encodeURIComponent(kw)+"&page=1",{headers:{"Referer":"https://www.bilibili.com/"}})
      .then(function(r){return r.json()}).then(function(d){
        var results=[]; (d.data&&d.data.result||[]).forEach(function(r){if(r.result_type==="video"&&r.data)results=results.concat(r.data);});
        if(!results.length){vArea.innerHTML='<div class="ss-empty">No videos</div>';return;}
        var vh='<div class="ss-video-grid">';
        results.slice(0,6).forEach(function(v){
          vh+='<div class="ss-video-item" data-bvid="'+(v.bvid||"")+'"><h4>'+esc((v.title||"").replace(/<[^>]+>/g,""))+'</h4><p>'+esc(v.author||"")+'</p><button class="ss-play-btn">Play</button></div>';
        });
        vh+='</div>'; vArea.innerHTML=vh;
        vArea.querySelectorAll("[data-bvid]").forEach(function(c){c.addEventListener("click",function(){
          var p=$(CONFIG.containers.player)||document.createElement("div"); p.style.display="block"; if(!p.parentNode) area.parentNode.insertBefore(p,area.nextSibling);
          biliResolve(c.getAttribute("data-bvid"),p);
        });});
      }).catch(function(){vArea.innerHTML='<div class="ss-error">Failed</div>';});
    // Music - inline iframe
    var mArea=$("ss-panel-music");
    var mEng=[{name:"NetEase",src:CONFIG.api.music163+encodeURIComponent(kw)},{name:"QQ",src:CONFIG.api.qqMusic+encodeURIComponent(kw)},{name:"Kugou",src:CONFIG.api.kugou+encodeURIComponent(kw)}];
    var mh='<div class="ss-engine-bar">'; mEng.forEach(function(e,i){mh+='<button class="'+(i===0?"active":"")+'" data-src="'+e.src+'">'+e.name+'</button>';});
    mh+='</div><iframe id="ss-music-frame" src="'+mEng[0].src+'" class="ss-iframe"></iframe>'; mArea.innerHTML=mh;
    mArea.querySelectorAll(".ss-engine-bar button").forEach(function(b){b.addEventListener("click",function(){
      mArea.querySelectorAll(".ss-engine-bar button").forEach(function(x){x.classList.remove("active")}); b.classList.add("active");
      $("ss-music-frame").src=b.getAttribute("data-src"); if(CONFIG.callbacks.onMusicPlay) CONFIG.callbacks.onMusicPlay(b.getAttribute("data-src"));
    });});
    // Article - inline iframe
    var aArea=$("ss-panel-article");
    var aEng=[{name:"Zhihu",url:CONFIG.engines.zhihu+encodeURIComponent(kw)},{name:"WeChat",url:CONFIG.engines.wechat+encodeURIComponent(kw)},{name:"Bing",url:CONFIG.engines.bing+encodeURIComponent(kw)}];
    var ah='<div class="ss-engine-bar">'; aEng.forEach(function(e,i){ah+='<button class="'+(i===0?"active":"")+'" data-url="'+e.url+'">'+e.name+'</button>';});
    ah+='</div><iframe id="ss-article-frame" src="'+aEng[0].url+'" class="ss-iframe ss-iframe-tall"></iframe>'; aArea.innerHTML=ah;
    aArea.querySelectorAll(".ss-engine-bar button").forEach(function(b){b.addEventListener("click",function(){
      aArea.querySelectorAll(".ss-engine-bar button").forEach(function(x){x.classList.remove("active")}); b.classList.add("active");
      $("ss-article-frame").src=b.getAttribute("data-url"); if(CONFIG.callbacks.onArticleOpen) CONFIG.callbacks.onArticleOpen(b.getAttribute("data-url"));
    });});
    // Web - Bing iframe
    $("ss-panel-web").innerHTML='<iframe src="'+CONFIG.engines.bing+encodeURIComponent(kw)+'" class="ss-iframe ss-iframe-tall"></iframe>';
    // AI
    var aiArea=$("ss-panel-ai");
    aiArea.innerHTML='<div class="ss-ai-box"><h4>Offline AI Sniffing</h4><p>Set UniversalSearch.config.aiBackend to enable.</p><button class="ss-btn ss-btn-ai" id="ss-ai-btn">Start Sniff</button></div>';
    var ab=$("ss-ai-btn"); if(ab) ab.addEventListener("click",function(){
      if(CONFIG.aiBackend){
        fetch(CONFIG.aiBackend,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({keyword:kw})})
          .then(function(r){return r.json()}).then(function(d){aiArea.innerHTML+='<pre class="ss-ai-result">'+esc(JSON.stringify(d,null,2))+'</pre>'; if(CONFIG.callbacks.onAiResult) CONFIG.callbacks.onAiResult(d);})
          .catch(function(){aiArea.innerHTML+='<p class="ss-error">Backend not responding</p>';});
      } else { aiArea.innerHTML+='<p class="ss-warning">Set config.aiBackend first</p>'; }
    });
  }

  function search(query, engine, options) {
    options=options||{}; var q=(query||"").trim(); if(!q) return;
    var video=detectVideo(q);
    if(video){ if(video.platform==="bilibili") biliResolve(q,options.playerArea); else showVideo(video,options.playerArea); return; }
    if(options.aggregate){ aggregateSearch(q,options.resultsArea); return; }
    var eng=engine||"bing"; var base=CONFIG.engines[eng]||CONFIG.engines.bing;
    // Inline display in iframe instead of opening new tab
    if(options.resultsArea){ options.resultsArea.style.display="block"; options.resultsArea.innerHTML='<iframe src="'+base+encodeURIComponent(q)+'" class="ss-iframe ss-iframe-tall"></iframe>'; return; }
    window.open(base+encodeURIComponent(q),"_blank");
  }

  function showVideo(video, area) {
    if(!area) area=$(CONFIG.containers.player)||document.createElement("div");
    area.style.display="block";
    area.innerHTML='<div class="ss-video-card"><h3>'+(video.platform||"Video")+' Detected</h3><div class="ss-video-actions"><a class="ss-btn ss-btn-primary" href="'+esc(video.url)+'" target="_blank">Play</a><button class="ss-btn ss-copy-btn">Copy</button></div><p class="ss-video-url">'+esc(video.url)+'</p></div>';
    var btn=area.querySelector(".ss-copy-btn"); if(btn) btn.addEventListener("click",function(){copyText(video.url);btn.textContent="Copied!";setTimeout(function(){btn.textContent="Copy";},1500);});
  }

  function init() {
    var input=$(CONFIG.containers.input), btn=$(CONFIG.containers.button), sel=$(CONFIG.containers.engine);
    function doSearch(){ if(!input) return; var hasResults=!!$(CONFIG.containers.results); search(input.value, sel?sel.value:"bing",{aggregate:hasResults,playerArea:$(CONFIG.containers.player),resultsArea:$(CONFIG.containers.results)}); }
    if(btn) btn.addEventListener("click",doSearch);
    if(input) input.addEventListener("keydown",function(e){if(e.key==="Enter")doSearch();});
  }
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",init); else init();

  global.UniversalSearch={ config:CONFIG, search:search, detectVideo:detectVideo, biliResolve:biliResolve, aggregate:aggregateSearch, copyText:copyText, version:"2.0.0" };
})(window);
