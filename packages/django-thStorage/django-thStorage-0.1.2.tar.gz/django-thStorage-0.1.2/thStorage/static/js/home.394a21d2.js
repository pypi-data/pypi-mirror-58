(function(t){function e(e){for(var i,r,s=e[0],l=e[1],c=e[2],d=0,u=[];d<s.length;d++)r=s[d],o[r]&&u.push(o[r][0]),o[r]=0;for(i in l)Object.prototype.hasOwnProperty.call(l,i)&&(t[i]=l[i]);p&&p(e);while(u.length)u.shift()();return n.push.apply(n,c||[]),a()}function a(){for(var t,e=0;e<n.length;e++){for(var a=n[e],i=!0,s=1;s<a.length;s++){var l=a[s];0!==o[l]&&(i=!1)}i&&(n.splice(e--,1),t=r(r.s=a[0]))}return t}var i={},o={home:0},n=[];function r(e){if(i[e])return i[e].exports;var a=i[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,r),a.l=!0,a.exports}r.m=t,r.c=i,r.d=function(t,e,a){r.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},r.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},r.t=function(t,e){if(1&e&&(t=r(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(r.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var i in t)r.d(a,i,function(e){return t[e]}.bind(null,i));return a},r.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},r.p="/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],l=s.push.bind(s);s.push=e,s=s.slice();for(var c=0;c<s.length;c++)e(s[c]);var p=l;n.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("9b06")},"0bb3":function(t,e,a){"use strict";var i=a("9029"),o=a.n(i);o.a},"2fbc":function(t,e,a){"use strict";var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-breadcrumb",{attrs:{separator:"/"}},t._l(t.items,function(e){return a("el-breadcrumb-item",{key:e.text},[a("a",{attrs:{href:e.url}},[t._v(t._s(e.text))])])}),1)},o=[],n={name:"Breadcrumb",props:{items:{type:Array,default:function(){return[]}}}},r=n,s=(a("3a6b"),a("2877")),l=Object(s["a"])(r,i,o,!1,null,"74860959",null);e["a"]=l.exports},"35a1":function(t,e,a){},"3a6b":function(t,e,a){"use strict";var i=a("fa39"),o=a.n(i);o.a},5240:function(t,e,a){t.exports=a.p+"static/img/default_icon_b.4d8feee1.png"},9029:function(t,e,a){},"9b06":function(t,e,a){"use strict";a.r(e);a("cadf"),a("551c"),a("f751"),a("097d");var i=a("2b0e"),o=a("ef55"),n=a.n(o),r=a("bc3a"),s=a.n(r),l=a("a7fe"),c=a.n(l),p=a("5c96"),d=a.n(p),u=(a("0fae"),a("35a1"),function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("Layout",[i("el-row",{attrs:{type:"flex",justify:"space-between"}},[i("el-col",{staticClass:"text-left",staticStyle:{"min-width":"330px"},attrs:{span:8}},[i("el-button",{staticClass:"icon-Upload-image",attrs:{type:"primary",plain:"",icon:"el-icon-upload2"},on:{click:t.openUploadDialog}},[t._v("上传")]),i("el-button",{attrs:{type:"primary",plain:"",icon:"el-icon-finished"},on:{click:function(e){return t.toggleSelect(t.tableData)}}},[t._v("全选")]),i("el-button",{attrs:{type:"primary",plain:"",icon:"el-icon-folder-add"},on:{click:function(e){t.dialogNewDir=!0}}},[t._v("新建文件夹")])],1),i("el-col",{staticClass:"text-right",staticStyle:{"min-width":"500px"},attrs:{span:16}},[i("el-button",{attrs:{disabled:0==t.selected.length,type:"primary",plain:"",icon:"el-icon-delete"},on:{click:t.batchDelete}},[t._v("删除")]),i("el-button",{attrs:{disabled:0==t.selected.length,type:"primary",plain:"",icon:"el-icon-document-copy"},on:{click:t.displayCopyTo}},[t._v("复制到")]),i("el-button",{attrs:{disabled:0==t.selected.length,type:"primary",plain:"",icon:"el-icon-top-right"},on:{click:t.displayCutTo}},[t._v("移动到")]),i("el-button",{staticClass:"checkpoints-operation-edit",attrs:{disabled:1!=t.selected.length,type:"primary",plain:"",icon:"el-icon-edit-outline"},on:{click:t.rename}},[t._v("重命名")])],1)],1),i("el-row",{staticStyle:{"margin-top":"20px",height:"31px"},attrs:{type:"flex",justify:"end"}},[i("el-col",{staticClass:"text-left",attrs:{span:2}},[i("el-link",{attrs:{type:"primary"},on:{click:function(e){return t.getList("back")}}},[t._v("返回上一级")]),i("el-link",{staticStyle:{"margin-left":"20px"},attrs:{type:"primary"},on:{click:function(e){return t.getList("refresh")}}},[t._v("刷新")])],1),i("el-col",{staticClass:"text-left",staticStyle:{"padding-top":"4px"},attrs:{span:20}},[i("el-breadcrumb",{staticStyle:{display:"inline-block"},attrs:{"separator-class":"el-icon-arrow-right"}},t._l(t.crumbList,function(e,a){return i("el-breadcrumb-item",{key:a},[0==a?i("a",{staticStyle:{cursor:"pointer"},on:{click:function(e){return t.getList("jump","",a)}}},[t._v("我的网盘")]):t._e(),0!=a?i("a",{staticStyle:{cursor:"pointer",display:"inline-block","white-space":"nowrap",overflow:"hidden","text-overflow":"ellipsis","max-width":"200px","text-align":"left"},on:{click:function(e){return t.getList("jump","",a)}}},[t._v(t._s(e.crumbName))]):t._e()])}),1)],1),i("el-col",{staticClass:"text-right",staticStyle:{"min-width":"300px"},attrs:{span:2}},[i("el-form",{staticClass:"demo-form-inline",attrs:{inline:!0}},[i("el-form-item",{attrs:{label:"|"}},[i("el-input",{staticClass:"bordernone",attrs:{placeholder:"搜索我的网盘文件"},on:{input:function(e){return t.change(e)}},model:{value:t.inputKeyword,callback:function(e){t.inputKeyword=e},expression:"inputKeyword"}})],1),i("el-form-item",[i("el-button",{attrs:{icon:"el-icon-search",type:"text"}})],1)],1)],1)],1),i("el-row",{staticStyle:{"text-align":"left",color:"#666666",padding:"0"}},[i("p",{staticStyle:{padding:"0!important","font-size":"13px"}},[t._v("共"+t._s(t.rawTableData.length)+"项  /  选中"+t._s(t.selected.length)+"项")])]),t.show1?i("el-row",[i("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.loading,expression:"loading"}],ref:"multipleTable",staticStyle:{width:"100%"},attrs:{"header-cell-style":t.getRowClass,height:"560",data:t.tableData,"row-style":{height:"50px"},"cell-style":{padding:"2px"},"highlight-current-row":"","default-sort":{prop:"date",order:"descending"}},on:{"selection-change":t.handleSelectionChange,"row-click":t.clickRow}},[i("el-table-column",{attrs:{type:"selection",width:"55"}}),i("el-table-column",{attrs:{prop:"name",label:"文件名",sortable:"","sort-method":t.sortMethodName,"min-width":"500"},scopedSlots:t._u([{key:"default",fn:function(e){return[i("div",{on:{contextmenu:function(e){return e.stopPropagation(),e.preventDefault(),t.$refs.ctxshow.showMenu(e)}}},[e.row.isDir?i("img",{staticStyle:{width:"20px"},attrs:{src:t.imgPathAgg.dir,alt:""}}):t._e(),e.row.isDir?t._e():i("img",{staticStyle:{width:"20px"},attrs:{src:t.imgPathAgg.file,alt:""}}),e.row.isDir?i("a",{staticStyle:{"margin-left":"10px",position:"absolute",top:"13px",cursor:"pointer",display:"inline-block","white-space":"nowrap",overflow:"hidden","text-overflow":"ellipsis","max-width":"400px","text-align":"left"},on:{click:function(a){return t.getList("enter",e.row.name)}}},[t._v(t._s(e.row.name))]):t._e(),e.row.isDir?t._e():i("a",{staticStyle:{"margin-left":"10px",position:"absolute",top:"13px",display:"inline-block","white-space":"nowrap",overflow:"hidden","text-overflow":"ellipsis","max-width":"400px","text-align":"left"}},[t._v(t._s(e.row.name))])])]}}],null,!1,3434513180)}),i("el-table-column",{attrs:{prop:"modify",label:"修改日期",sortable:"",width:"180","sort-method":t.sortMethodDate}}),i("el-table-column",{attrs:{prop:"size",formatter:t.fmtSize,label:"大小",width:"180",sortable:"","sort-method":t.sortMethodSize}}),i("el-table-column",{attrs:{prop:"operation",label:"操作",width:"180",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[i("el-tooltip",{staticClass:"item",attrs:{effect:"dark",content:"删除",placement:"top"}},[i("el-button",{staticStyle:{"margin-right":"20px"},attrs:{type:"text",size:"medium",icon:"el-icon-delete"},on:{click:function(a){return t.unitDelete(e.row.name)}}})],1),i("el-tooltip",{staticClass:"item",attrs:{effect:"dark",content:"下载",placement:"top"}},[i("el-button",{attrs:{type:"text",size:"medium",icon:"el-icon-download"},on:{click:function(a){return t.unitDownload(e.row.name,e.row.isDir)}}})],1)]}}],null,!1,4162660115)})],1),i("e-vue-contextmenu",{ref:"ctxshow",attrs:{id:"contextStyle"},on:{"ctx-show":t.show,"ctx-hide":t.hide}},[i("el-button",{staticClass:"list-button",attrs:{disabled:1!=t.selected.length},on:{click:t.openR}},[t._v("打开文件夹")]),i("hr"),i("el-button",{staticClass:"list-button",attrs:{disabled:0==t.selected.length},on:{click:t.displayCopyToR}},[t._v("复制到")]),i("el-button",{staticClass:"list-button",attrs:{disabled:0==t.selected.length},on:{click:t.displayCutToR}},[t._v("移动到")]),i("el-button",{staticClass:"list-button",attrs:{disabled:0==t.selected.length},on:{click:t.batchDeleteR}},[t._v("删除")]),i("el-button",{staticClass:"list-button",attrs:{disabled:1!=t.selected.length},on:{click:t.renameR}},[t._v("重命名")]),i("hr"),i("el-button",{staticClass:"list-button",attrs:{disabled:1!=t.selected.length},on:{click:t.attributeR}},[t._v("属性")]),i("el-button",{staticClass:"list-button",on:{click:t.refreshR}},[t._v("刷新")])],1)],1):t._e(),t.show2?i("el-row",[i("div",{staticClass:"circle"},[i("ul",{staticClass:"circle-ul"},[t._l(t.inputArr,function(e){return i("li",{key:e.id,staticClass:"circle-li",on:{contextmenu:function(e){return e.stopPropagation(),e.preventDefault(),t.$refs.ctxshow.showMenu(e)}}},[i("div",[i("el-checkbox",{on:{"selection-change":t.handleSelectionChange},model:{value:e.checked,callback:function(a){t.$set(e,"checked",a)},expression:"item.checked"}},[i("img",{staticStyle:{width:"80px",height:"80px"},attrs:{src:e.coverImg}}),i("p",{staticStyle:{padding:"0",margin:"0",width:"70px","vertical-align":"middle","line-height":"12px","white-space":"nowrap","text-overflow":"ellipsis",overflow:"hidden","text-align":"center"},domProps:{innerHTML:t._s(e.title)}})])],1)])}),i("e-vue-contextmenu",{ref:"ctxshow",attrs:{id:"contextStyle"},on:{"ctx-show":t.show,"ctx-hide":t.hide}},[i("el-button",{staticClass:"list-button",attrs:{disabled:0==t.selected.length}},[t._v("打开文件夹")]),i("hr"),i("el-button",{staticClass:"list-button",attrs:{disabled:0==t.selected.length},on:{click:function(e){t.dialogCatalogue=!0}}},[t._v("复制到")]),i("el-button",{staticClass:"list-button",attrs:{disabled:0==t.selected.length},on:{click:function(e){t.dialogCatalogue=!0}}},[t._v("移动到")]),i("el-button",{staticClass:"list-button",attrs:{disabled:0==t.selected.length},on:{click:t.batchDelete}},[t._v("删除")]),i("el-button",{staticClass:"list-button",attrs:{disabled:1!=t.selected.length},on:{click:t.rename}},[t._v("重命名")]),i("hr"),i("el-button",{staticClass:"list-button",attrs:{disabled:0==t.selected.length},on:{click:function(e){t.dialogAttribute=!0}}},[t._v("属性")]),i("el-button",{staticClass:"list-button",attrs:{disabled:0==t.selected.length}},[t._v("刷新")])],1)],2)])]):t._e(),i("el-dialog",{staticClass:"add-dialog",staticStyle:{"text-align":"left"},attrs:{title:"上传",visible:t.dialogUpload,width:"50%"},on:{"update:visible":function(e){t.dialogUpload=e}}},[i("uploader",{ref:"uploader",staticClass:"uploader-example",attrs:{options:t.options}},[i("uploader-unsupport"),i("uploader-btn",{staticStyle:{"margin-bottom":"20px"}},[t._v("上传文件")]),i("uploader-list")],1)],1),i("el-dialog",{staticStyle:{"text-align":"left"},attrs:{title:"属性",visible:t.dialogAttribute,width:"30%"},on:{"update:visible":function(e){t.dialogAttribute=e}}},[i("el-card",{attrs:{shadow:"never"}},[i("el-row",{staticStyle:{"border-bottom":"1px dashed #e5e5e5","padding-bottom":"20px"}},[t.attributeInfo.isDir?i("img",{staticStyle:{float:"left",border:"1px solid #e5e5e5",padding:"10px"},attrs:{src:t.imgPathAgg.dir,alt:""}}):t._e(),t.attributeInfo.isDir?t._e():i("img",{staticStyle:{float:"left",border:"1px solid #e5e5e5",padding:"10px"},attrs:{src:t.imgPathAgg.file,alt:""}}),i("h3",{staticStyle:{float:"left","padding-top":"20px","margin-left":"20px"}},[t._v(t._s(t.attributeInfo.location))])]),i("el-row",[i("p",[i("strong",[t._v("名称：")]),t._v(t._s(t.attributeInfo.name))]),t.attributeInfo.isDir?i("p",[i("strong",[t._v("类型：")]),t._v("目录")]):t._e(),t.attributeInfo.isDir?t._e():i("p",[i("strong",[t._v("类型：")]),t._v("文件")]),i("p",[i("strong",[t._v("大小：")]),t._v(t._s(t.attributeInfo.size))]),i("p",[i("strong",[t._v("修改时间：")]),t._v(t._s(t.attributeInfo.modify))])])],1)],1),i("el-dialog",{directives:[{name:"loading",rawName:"v-loading",value:t.loadingDialogTo,expression:"loadingDialogTo"}],staticStyle:{"text-align":"left"},attrs:{title:"文件目录",visible:t.dialogCatalogue,width:"550px"},on:{"update:visible":function(e){t.dialogCatalogue=e}}},[i("div",{staticClass:"border"},[i("el-row",{attrs:{type:"flex",justify:"end"}},[i("el-col",{staticClass:"text-left"},[i("el-button",{attrs:{type:"text",icon:"el-icon-arrow-left"},on:{click:function(e){return t.getListTo("back")}}}),i("el-button",{attrs:{type:"text",icon:"el-icon-refresh"},on:{click:function(e){return t.getListTo("refresh")}}}),i("el-button",{attrs:{type:"text",icon:"el-icon-arrow-right"},on:{click:function(e){return t.getListTo("forward")}}}),i("el-breadcrumb",{staticStyle:{display:"inline-block","margin-left":"50px"},attrs:{"separator-class":"el-icon-arrow-right"}},t._l(t.crumbListTo,function(e,a){return i("el-breadcrumb-item",{key:a},[0==a?i("a",{staticStyle:{cursor:"pointer"},on:{click:function(e){return t.getListTo("jump","",a)}}},[t._v("我的网盘")]):t._e(),0!=a?i("a",{staticStyle:{cursor:"pointer",display:"inline-block","white-space":"nowrap",overflow:"hidden","text-overflow":"ellipsis","max-width":"100px","text-align":"left"},on:{click:function(e){return t.getListTo("jump","",a)}}},[t._v(t._s(e.crumbName))]):t._e()])}),1)],1)],1),i("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.loadingTo,expression:"loadingTo"}],ref:"singleTable",staticStyle:{width:"100%"},attrs:{"header-cell-style":t.getRowClass,data:t.tableDataTo,"highlight-current-row":"",height:"400"},on:{"current-change":t.handleCurrentChange}},[i("el-table-column",{attrs:{prop:"name",label:"文件名"},scopedSlots:t._u([{key:"default",fn:function(e){return[i("div",{on:{contextmenu:function(e){return e.stopPropagation(),e.preventDefault(),t.$refs.ctxshow.showMenu(e)}}},[e.row.isDir?i("img",{staticStyle:{width:"20px"},attrs:{src:t.imgPathAgg.dir,alt:""}}):t._e(),e.row.isDir?t._e():i("img",{staticStyle:{width:"20px"},attrs:{src:t.imgPathAgg.file,alt:""}}),e.row.isDir?i("a",{staticStyle:{"margin-left":"30px",position:"absolute",top:"13px",overflow:"hidden","text-overflow":"ellipsis",display:"-webkit-box","-webkit-line-clamp":"1","-webkit-box-orient":"vertical"},on:{click:function(a){return t.getListTo("enter",e.row.name)}}},[t._v(t._s(e.row.name))]):t._e(),e.row.isDir?t._e():i("a",{staticStyle:{"margin-left":"30px",position:"absolute",top:"13px",overflow:"hidden","text-overflow":"ellipsis",display:"-webkit-box","-webkit-line-clamp":"1","-webkit-box-orient":"vertical"}},[t._v(t._s(e.row.name))])])]}}])}),i("el-table-column",{attrs:{prop:"modify",label:"修改日期",width:"180"}})],1)],1),i("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{on:{click:function(e){t.dialogCatalogue=!1}}},[t._v("取 消")]),i("el-button",{attrs:{type:"primary"},on:{click:t.confirmTo}},[t._v("确 定")])],1)]),i("el-dialog",{staticStyle:{"text-align":"left"},attrs:{title:"新增文件夹",visible:t.dialogNewDir,width:"450px"},on:{"update:visible":function(e){t.dialogNewDir=e}}},[i("el-form",[i("el-row",[i("el-col",{staticStyle:{width:"100px"}},[i("img",{attrs:{src:a("f96f"),height:"72",width:"72"}})]),i("el-col",{staticStyle:{width:"300px","margin-top":"20px"}},[i("el-form-item",[i("el-input",{attrs:{placeholder:"请输入文件夹名称"},model:{value:t.inputNewDir,callback:function(e){t.inputNewDir=e},expression:"inputNewDir"}})],1)],1)],1)],1),i("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{on:{click:function(e){t.dialogNewDir=!1}}},[t._v("取 消")]),i("el-button",{attrs:{type:"primary"},on:{click:t.addNewDirConfirm}},[t._v("确 定")])],1)],1),i("el-dialog",{staticStyle:{"text-align":"left"},attrs:{title:"重命名",visible:t.dialogRename,width:"450px"},on:{"update:visible":function(e){t.dialogRename=e}}},[i("el-form",[i("el-row",[i("el-col",{staticStyle:{width:"100px"}},[t.inputRenameType?i("img",{attrs:{src:a("f96f"),height:"72",width:"72"}}):t._e(),t.inputRenameType?t._e():i("img",{attrs:{src:a("5240"),height:"72",width:"72"}})]),i("el-col",{staticStyle:{width:"70%","margin-top":"20px"}},[i("el-form-item",[i("el-input",{attrs:{placeholder:"请输入文件/文件夹名称"},model:{value:t.inputRename,callback:function(e){t.inputRename=e},expression:"inputRename"}})],1)],1)],1)],1),i("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{on:{click:function(e){t.dialogRename=!1}}},[t._v("取 消")]),i("el-button",{attrs:{type:"primary"},on:{click:t.renameConfirm}},[t._v("确 定")])],1)],1),i("el-dialog",{staticStyle:{"text-align":"left"},attrs:{title:"传输失败文件列表",visible:t.dialogToFailed,width:"450px","close-on-click-modal":!1,"close-on-press-escape":!1},on:{"update:visible":function(e){t.dialogToFailed=e}}},[i("el-table",{ref:"singleTable",staticStyle:{width:"100%"},attrs:{"header-cell-style":t.getRowClass,data:t.tableDataToFailed,"highlight-current-row":"",height:"400"}},[i("el-table-column",{attrs:{prop:"name",label:"文件名"}}),i("el-table-column",{attrs:{prop:"reason",label:"失败原因",width:"180"}})],1)],1),i("el-dialog",{staticStyle:{"text-align":"left"},attrs:{title:"上传失败文件列表",visible:t.dialogUploadFailed,width:"450px","close-on-click-modal":!1,"close-on-press-escape":!1,"before-close":t.uploadDialogClose},on:{"update:visible":function(e){t.dialogUploadFailed=e}}},[i("el-table",{ref:"singleTable",staticStyle:{width:"100%"},attrs:{"header-cell-style":t.getRowClass,data:t.tableDataUploadFailed,"highlight-current-row":"",height:"400"}},[i("el-table-column",{attrs:{prop:"name",label:"文件名"}}),i("el-table-column",{attrs:{prop:"reason",label:"失败原因",width:"180"}})],1)],1)],1)}),h=[],m=(a("456d"),a("96cf"),a("3b8d")),f=(a("ac6a"),a("a481"),a("7f7f"),a("ebad")),g=a("2fbc"),b=a("6c27").sha256,w=a("df7c"),y=window.localStorage,v={name:"home",components:{Layout:f["a"],Breadcrumb:g["a"]},created:function(){var t=y.getItem("nowPath"),e=JSON.parse(y.getItem("pathHistory")),a=parseInt(y.getItem("pathHistoryCursor")),i=JSON.parse(y.getItem("crumbList")),o=y.getItem("token");""==y.getItem("platform")||y.getItem("platform");this.nowPath=t||"/",e&&(this.pathHistory=e),a&&(this.pathHistoryCursor=a),i&&(this.crumbList=i),this.token=o||"",this.getList("refresh",this.nowPath),this.getCapacity()},data:function(){return{options:{},uploaderInter:"",tableDataUploadFailed:[],uploading:!1,timestamp:"",loading:!1,loadingTo:!1,loadingDialogTo:!1,loadingDialogDelete:!1,imgPathAgg:{dir:a("f96f"),file:a("5240")},nowPathTo:"/",pathHistoryTo:["/"],pathHistoryCursorTo:0,crumbListTo:[{crumbName:"/",crumbPath:"/"}],tableDataTo:[],tableDataToFailed:[],dialogCatalogue:!1,currentRow:null,operationTo:"",nowPath:"/",pathHistory:["/"],pathHistoryCursor:0,crumbList:[{crumbName:"/",crumbPath:"/"}],inputKeyword:"",inputNewDir:"",inputRename:"",inputRenameType:"",inputArr:[{id:"001",coverImg:a("f96f"),title:"文件姓名文件姓名文件姓名文件姓名1",checked:"false"}],selected:[],button1:"primary",button2:"",rawTableData:[],tableData:[],attributeInfo:{},dialogAttribute:!1,dialogNewDir:!1,dialogRename:!1,dialogUpload:!1,dialogToFailed:!1,dialogUploadFailed:!1,show1:!0,show2:!1,show:"",hide:"",breadcrumb_items:[{text:"网盘首页",url:"/page1/"}],capacityUsed:0,capacityTotal:0,capacityPercentage:0}},methods:{openR:function(){this.hideMenu(),this.getList("enter",this.selected[0].name)},batchDownloadR:function(){this.hideMenu(),this.batchDownload()},displayCopyToR:function(){this.hideMenu(),this.displayCopyTo()},displayCutToR:function(){this.hideMenu(),this.displayCutTo()},batchDeleteR:function(){this.hideMenu(),this.batchDelete()},renameR:function(){this.hideMenu(),this.rename()},refreshR:function(){this.hideMenu(),this.getList("refresh")},attributeR:function(){var t=this;this.hideMenu(),this.loading=!0;var e=Math.round(new Date/1e3),a=b(this.token+e),i=w.join(this.nowPath,this.selected[0].name).replace("\\","/"),o=new URLSearchParams;o.append("platform",y.getItem("platform")),o.append("username",y.getItem("username")),o.append("cluster",y.getItem("cluster")),o.append("encrypedToken",a),o.append("timestamp",e),o.append("path",i),this.axios({method:"post",url:"/attribute/",data:o}).then(function(e){"no"==e.data.success?(t.loading=!1,alert(e.data.error_desc)):(t.loading=!1,t.attributeInfo=e.data.attribute,t.attributeInfo.name=t.selected[0].name,t.attributeInfo.location=i,t.attributeInfo.isDir?t.attributeInfo.size="-":void 0===t.attributeInfo.size?t.attributeInfo.size=0:t.attributeInfo.size=t.compFmtSize(t.attributeInfo.size),t.dialogAttribute=!0)}).catch(function(e){t.loading=!1,alert(e)})},displayCopyTo:function(){this.operationTo="copy",this.displayTo()},displayCutTo:function(){this.operationTo="cut",this.displayTo()},displayTo:function(){var t=y.getItem("nowPathTo"),e=JSON.parse(y.getItem("pathHistoryTo")),a=parseInt(y.getItem("pathHistoryCursorTo")),i=JSON.parse(y.getItem("crumbListTo"));t&&(this.nowPathTo=t),e&&(this.pathHistoryTo=e),a&&(this.pathHistoryCursorTo=a),i&&(this.crumbListTo=i),this.getListTo("refresh",this.nowPathTo),this.dialogCatalogue=!0},confirmTo:function(){var t=this;if(this.currentRow&&!this.currentRow.isDir)return alert("目的地址不能是文件"),1;this.loadingDialogTo=!0;var e=Math.round(new Date/1e3),a=b(this.token+e),i="",o="";this.selected.forEach(function(e){i=w.join(t.nowPath,e.name).replace("\\","/"),o=o+i+","});var n="";n=this.currentRow?w.join(this.nowPathTo,this.currentRow.name).replace("\\","/"):this.nowPathTo;var r=new URLSearchParams;r.append("platform",y.getItem("platform")),r.append("username",y.getItem("username")),r.append("cluster",y.getItem("cluster")),r.append("encrypedToken",a),r.append("timestamp",e),r.append("oldPathList",o),r.append("newPath",n);var s="",l="";"copy"==this.operationTo?(s="/copyTo/",l="拷贝成功"):"cut"==this.operationTo&&(s="/cutTo/",l="移动成功"),this.axios({method:"post",url:s,data:r}).then(function(e){"no"==e.data.success?(t.dialogCatalogue=!1,t.loadingDialogTo=!1,alert(e.data.error_desc)):(t.nowPathTo="/",t.pathHistoryTo=["/"],t.pathHistoryCursorTo=0,t.crumbListTo=[{crumbName:"/",crumbPath:"/"}],t.tableDataTo=[],t.dialogCatalogue=!1,t.getList("refresh"),y.setItem("nowPathTo",t.nowPathTo),y.setItem("pathHistoryTo",JSON.stringify(t.pathHistoryTo)),y.setItem("pathHistoryCursorTo",t.pathHistoryCursorTo),y.setItem("crumbListTo",JSON.stringify(t.crumbListTo)),t.loadingDialogTo=!1,0==e.data.failedList.length?t.$message({type:"success",message:l}):(t.tableDataToFailed=e.data.failedList,t.dialogToFailed=!0))}).catch(function(e){t.loadingDialogTo=!1,t.dialogCatalogue=!1,alert(e)})},handleCurrentChange:function(t){this.currentRow=t},getListTo:function(){var t=this,e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"",i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";if("back"==e&&0==this.pathHistoryCursorTo)return 0;if("forward"==e&&this.pathHistoryCursorTo==this.pathHistoryTo.length-1)return 0;this.loadingTo=!0;var o=Math.round(new Date/1e3),n=b(this.token+o),r="";r="back"==e?this.pathHistoryTo[this.pathHistoryCursorTo-1]:"forward"==e?this.pathHistoryTo[this.pathHistoryCursorTo+1]:"refresh"==e?this.pathHistoryTo[this.pathHistoryCursorTo]:"jump"==e?this.pathHistoryTo[i]:w.join(this.nowPathTo,a).replace("\\","/");var s=new URLSearchParams;s.append("platform",y.getItem("platform")),s.append("username",y.getItem("username")),s.append("cluster",y.getItem("cluster")),s.append("encrypedToken",n),s.append("timestamp",o),s.append("path",r),this.axios({method:"POST",url:"/list/",data:s}).then(function(a){if("no"==a.data.success)return t.tableDataTo=[],t.loadingTo=!1,alert(a.data.error_desc),0;t.tableDataTo=a.data.listContent,t.nowPathTo=r,"back"==e?(t.pathHistoryCursorTo-=1,t.crumbListTo.pop()):"forward"==e?(t.pathHistoryCursorTo+=1,t.crumbListTo.push({crumbName:w.basename(r),crumbPath:r})):"refresh"==e||("jump"==e?(t.pathHistoryTo=t.pathHistoryTo.slice(0,i+1),t.crumbListTo=t.crumbListTo.slice(0,i+1),t.pathHistoryCursorTo=i):(t.pathHistoryCursorTo<t.pathHistoryTo.length-1&&(t.pathHistoryTo=t.pathHistoryTo.slice(0,t.pathHistoryCursorTo+1)),t.pathHistoryTo.push(r),t.crumbListTo.push({crumbName:w.basename(r),crumbPath:r}),t.pathHistoryCursorTo+=1)),y.setItem("nowPathTo",t.nowPathTo),y.setItem("pathHistoryTo",JSON.stringify(t.pathHistoryTo)),y.setItem("pathHistoryCursorTo",t.pathHistoryCursorTo),y.setItem("crumbListTo",JSON.stringify(t.crumbListTo)),t.loadingTo=!1}).catch(function(e){t.loadingTo=!1,alert(e)})},getCapacity:function(){var t=this,e=Math.round(new Date/1e3),a=b(this.token+e),i=new URLSearchParams;i.append("platform",y.getItem("platform")),i.append("username",y.getItem("username")),i.append("cluster",y.getItem("cluster")),i.append("encrypedToken",a),i.append("timestamp",e),this.axios({method:"post",url:"/capacity/",data:i}).then(function(e){"no"==e.data.success?alert(e.data.error_desc):(t.capacityUsed=(e.data.capacity.usedCapacity/1024/1024/1024).toFixed(2),t.capacityTotal=(e.data.capacity.totalCapacity/1024/1024/1024).toFixed(2),t.capacityPercentage=parseInt((100*t.capacityUsed/t.capacityTotal).toFixed(2)))}).catch(function(t){alert(t)})},getList:function(){var t=this,e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"",i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"";if("back"==e&&0==this.pathHistoryCursor)return 0;if("forward"==e&&this.pathHistoryCursor==this.pathHistory.length-1)return 0;this.loading=!0;var o=Math.round(new Date/1e3),n=b(this.token+o),r="";r="back"==e?this.pathHistory[this.pathHistoryCursor-1]:"forward"==e?this.pathHistory[this.pathHistoryCursor+1]:"refresh"==e?this.pathHistory[this.pathHistoryCursor]:"jump"==e?this.pathHistory[i]:w.join(this.nowPath,a).replace("\\","/");var s=new URLSearchParams;s.append("platform",y.getItem("platform")),s.append("username",y.getItem("username")),s.append("cluster",y.getItem("cluster")),s.append("encrypedToken",n),s.append("timestamp",o),s.append("path",r),this.axios({method:"POST",url:"/list/",data:s}).then(function(a){if("no"==a.data.success)return t.tableData=[],t.loading=!1,alert(a.data.error_desc),0;t.rawTableData=a.data.listContent,t.tableData=t.rawTableData,t.nowPath=r,"back"==e?(t.pathHistoryCursor-=1,t.crumbList.pop()):"forward"==e?(t.pathHistoryCursor+=1,t.crumbList.push({crumbName:w.basename(r),crumbPath:r})):"refresh"==e||("jump"==e?(t.pathHistory=t.pathHistory.slice(0,i+1),t.crumbList=t.crumbList.slice(0,i+1),t.pathHistoryCursor=i):(t.pathHistoryCursor<t.pathHistory.length-1&&(t.pathHistory=t.pathHistory.slice(0,t.pathHistoryCursor+1)),t.pathHistory.push(r),t.crumbList.push({crumbName:w.basename(r),crumbPath:r}),t.pathHistoryCursor+=1)),y.setItem("nowPath",t.nowPath),y.setItem("pathHistory",JSON.stringify(t.pathHistory)),y.setItem("pathHistoryCursor",t.pathHistoryCursor),y.setItem("crumbList",JSON.stringify(t.crumbList)),t.loading=!1}).catch(function(e){t.loading=!1,alert(e)})},sortMethodName:function(t,e){if(t.isDir&&e.isDir)t.name.localeCompare(e.name,"zh-CN");else{if(t.isDir)return-1;if(e.isDir)return 1}return t.name.localeCompare(e.name,"zh-CN")},sortMethodDate:function(t,e){return t.isDir&&e.isDir?0:t.isDir?-1:e.isDir?1:void 0},sortMethodSize:function(t,e){return t.isDir&&e.isDir?0:t.isDir?-1:e.isDir?1:t.size||e.size?t.size?e.size?parseInt(t.size)>parseInt(e.size)?1:parseInt(t.size)<parseInt(e.size)?-1:0:1:-1:0},compFmtSize:function(t){var e=1024,a=1048576,i=1073741824,o=1099511627776,n=0x4000000000000,r=t;return void 0===r?"0":(r<e?r+="B":r<a?r=Math.round(100*r/1024)/100+"KB":r<i?r=Math.round(100*r/1024/1024)/100+"MB":r<o?r=Math.round(100*r/1024/1024/1024)/100+"GB":r<n&&(r=Math.round(100*r/1024/1024/1024/1024)/100+"TB"),r)},fmtSize:function(t,e,a,i){if(t["isDir"]){var o="-";return o}var n=t[e.property];return void 0===n?"0":(n=this.compFmtSize(n),n)},rename:function(){this.inputRename=this.selected[0].name,this.inputRenameType=this.selected[0].isDir,this.hideMenu(),this.dialogRename=!0},renameConfirm:function(){var t=this;this.loading=!0;var e=Math.round(new Date/1e3),a=b(this.token+e),i=new URLSearchParams,o=this.selected[0].name,n=this.inputRename,r=this.nowPath;return-1!=n.indexOf("/")||-1!=n.indexOf("\\")?(this.loading=!1,alert("名称中不能包含\\或/"),1):0==n.length?(this.loading=!1,alert("文件/文件夹名称不能为空"),1):n.length>64?(this.loading=!1,alert("名称长度不能超过64"),1):(i.append("platform",y.getItem("platform")),i.append("username",y.getItem("username")),i.append("cluster",y.getItem("cluster")),i.append("encrypedToken",a),i.append("timestamp",e),i.append("path",r),i.append("oldName",o),i.append("newName",n),void this.axios({method:"post",url:"/rename/",data:i}).then(function(e){"no"==e.data.success?(t.dialogRename=!1,t.loading=!1,alert(e.data.error_desc)):(t.loading=!1,t.dialogRename=!1,t.inputRename="",t.inputRenameType="",t.getList("refresh"),t.$message({type:"success",message:"重命名成功!"}))}).catch(function(e){t.loading=!1,t.dialogRename=!1,alert(e)}))},renameUpload:function(){var t=Object(m["a"])(regeneratorRuntime.mark(function t(){var e,a,i,o,n,r,s=this,l=arguments;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:return e=l.length>0&&void 0!==l[0]?l[0]:"",a=l.length>1&&void 0!==l[1]?l[1]:"",i=l.length>2&&void 0!==l[2]?l[2]:"",o=Math.round(new Date/1e3),n=b(this.token+o),r=new URLSearchParams,r.append("platform",y.getItem("platform")),r.append("username",y.getItem("username")),r.append("cluster",y.getItem("cluster")),r.append("encrypedToken",n),r.append("timestamp",o),r.append("path",i),r.append("oldName",e),r.append("newName",a),t.next=16,this.axios({method:"post",url:"/rename/",data:r}).then(function(t){if("no"==t.data.success){var e=a,i=t.data.error_desc;s.tableDataUploadFailed.push({name:e,reason:i})}else s.getList("refresh")}).catch(function(t){var e=a,i=t;s.tableDataUploadFailed.push({name:e,reason:i})});case 16:case"end":return t.stop()}},t,this)}));function e(){return t.apply(this,arguments)}return e}(),addNewDirConfirm:function(){var t=this;this.loading=!0;var e=Math.round(new Date/1e3),a=b(this.token+e),i=new URLSearchParams,o=this.inputNewDir,n=w.join(this.nowPath,o).replace("\\","/");return-1!=o.indexOf("/")||-1!=o.indexOf("\\")?(this.loading=!1,alert("文件夹名称中不能包含\\或/"),1):0==o.length?(this.loading=!1,alert("文件夹名称不能为空"),1):o.length>64?(this.loading=!1,alert("文件夹名称长度不能超过64"),1):(i.append("platform",y.getItem("platform")),i.append("username",y.getItem("username")),i.append("cluster",y.getItem("cluster")),i.append("encrypedToken",a),i.append("timestamp",e),i.append("path",n),void this.axios({method:"post",url:"/newfolder/",data:i}).then(function(e){"no"==e.data.success?(t.dialogNewDir=!1,t.loading=!1,alert(e.data.error_desc)):(t.loading=!1,t.dialogNewDir=!1,t.inputNewDir="",t.getList("refresh"),t.$message({type:"success",message:"新建文件夹成功!"}))}).catch(function(e){t.dialogNewDir=!1,t.loading=!1,alert(e)}))},batchDelete:function(){var t=this;this.$confirm("此操作将删除所有选中的文件和目录, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){t.loading=!0;var e=Math.round(new Date/1e3),a=b(t.token+e),i="",o="";t.selected.forEach(function(e){i=w.join(t.nowPath,e.name).replace("\\","/"),o=o+i+","});var n=new URLSearchParams;n.append("platform",y.getItem("platform")),n.append("username",y.getItem("username")),n.append("cluster",y.getItem("cluster")),n.append("encrypedToken",a),n.append("timestamp",e),n.append("serverPathList",o),t.axios({method:"post",url:"/delete/",data:n}).then(function(e){"no"==e.data.success?(t.loading=!1,alert(e.data.error_desc)):(t.getList("refresh"),t.loading=!1,t.$message({type:"success",message:"删除成功!"}))}).catch(function(e){t.loading=!1,alert(e.response.data.error)})}).catch(function(){t.$message({type:"info",message:"已取消删除"})})},unitDelete:function(t){var e=this;this.$confirm("此操作将删除此文件, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){e.loading=!0;var a=Math.round(new Date/1e3),i=b(e.token+a),o=w.join(e.nowPath,t).replace("\\","/"),n=new URLSearchParams;n.append("platform",y.getItem("platform")),n.append("username",y.getItem("username")),n.append("cluster",y.getItem("cluster")),n.append("encrypedToken",i),n.append("timestamp",a),n.append("serverPathList",o),e.axios({method:"post",url:"/delete/",data:n}).then(function(t){"no"==t.data.success?(e.loading=!1,alert(t.data.error_desc)):(e.loading=!1,e.getList("refresh"),e.$message({type:"success",message:"删除成功!"}))}).catch(function(t){e.loading=!1,alert(t.response.data.error)})}).catch(function(){e.$message({type:"info",message:"已取消删除"})})},tmpFileDelete:function(t){var e=this,a=Math.round(new Date/1e3),i=b(this.token+a),o=t,n=new URLSearchParams;n.append("platform",y.getItem("platform")),n.append("username",y.getItem("username")),n.append("cluster",y.getItem("cluster")),n.append("encrypedToken",i),n.append("timestamp",a),n.append("serverPathList",o),this.axios({method:"post",url:"/delete/",data:n}).then(function(t){e.getList("refresh")}).catch(function(t){console.log(t.response.data.error)})},downloadDir:function(t){var e=this,a=Math.round(new Date/1e3),i=b(this.token+a),o=new URLSearchParams;o.append("platform",y.getItem("platform")),o.append("username",y.getItem("username")),o.append("cluster",y.getItem("cluster")),o.append("encrypedToken",i),o.append("timestamp",a),o.append("path",t),this.axios({method:"POST",url:"/list/",data:o}).then(function(a){var i=a.data.listContent;i.forEach(function(a){if(a.isDir){var i=w.join(t,a.name).replace("\\","/");e.downloadDir(i)}else if(!a.isDir){var o=w.join(t,a.name).replace("\\","/");e.downloadFile(o)}})}).catch(function(t){e.loading=!1,alert(t)})},downloadFile:function(t){var e=Math.round(new Date/1e3),a=b(this.token+e),i=window.location.protocol+"//"+window.location.host,o=decodeURI(i+"/webDownloadFile?platform="+y.getItem("platform")+"&username="+y.getItem("username")+"&cluster="+y.getItem("cluster")+"&encrypedToken="+String(a)+"&timestamp="+String(e)+"&serverPath="+String(t));console.log(o),window.location.href=o},batchDownload:function(){var t=this,e=!1;this.selected.forEach(function(t){t.isDir&&(e=!0)}),e?alert("暂不支持对文件夹进行下载。"):this.selected.forEach(function(e){var a=w.join(t.nowPath,e.name).replace("\\","/");e.isDir?t.downloadDir(a):e.isDir||t.downloadFile(a)})},unitDownload:function(t,e){e?alert("暂不支持对目录进行下载。"):e?alert("unknown download type."):this.unitDownloadFile(t)},unitDownloadDir:function(t){var e=w.join(this.nowPath,t).replace("\\","/");this.downloadDir(e)},unitDownloadFile:function(t){var e=w.join(this.nowPath,t).replace("\\","/");this.downloadFile(e)},clickRow:function(t,e,a){"operation"!=e.property&&this.$refs.multipleTable.toggleRowSelection(t)},handleSelectionChange:function(t){this.selected=t},toggleSelect:function(t){var e=this;t&&(t.length==this.selected.length?t.forEach(function(t){e.$refs.multipleTable.toggleRowSelection(t,!1)}):t.forEach(function(t){e.$refs.multipleTable.toggleRowSelection(t,!0)}))},getRowClass:function(t){t.row,t.column;var e=t.rowIndex;t.columnIndex;return 0===e?"border-top: 1px solid #ebeef5;":""},gotolink:function(){window.location.href="/recycle"+this.urlParam},showCont1:function(){this.show1=!0,this.show2=!1,this.button1="primary",this.button2=""},showCont2:function(){this.show2=!0,this.show1=!1,this.button1="",this.button2="primary"},hideMenu:function(){this.$refs.ctxshow.hideMenu()},change:function(t){var e=this;this.tableData=this.rawTableData.filter(function(t){return Object.keys(t).some(function(a){return String(t[a]).toLowerCase().indexOf(e.inputKeyword.toLowerCase())>-1})})},uploadDialogClose:function(t){this.tableDataUploadFailed=[],t()},openUploadDialog:function(){var t=this;this.dialogUpload=!0;var e=Math.round(new Date/1e3),a=b(this.token+e),i=this.nowPath;try{var o=this.$refs.uploader.uploader;this.uploading&&i!=o.opts.query.serverPath?alert("当前有正在上传的任务，不能更换上传目录。如此时上传文件，则仍将上传到"+o.opts.query.serverPath+"目录下"):o.opts.query.serverPath=i,o.opts.query.platform=y.getItem("platform"),o.opts.query.username=y.getItem("username"),o.opts.query.timestamp=e,o.opts.query.encrypedToken=a}catch(r){this.options={target:"/webUploadFile/",testChunks:!1,allowDuplicateUploads:!0,simultaneousUploads:1,query:{platform:y.getItem("platform"),username:y.getItem("username"),cluster:y.getItem("cluster"),timestamp:e,encrypedToken:a,serverPath:i}};var n=setInterval(function(){try{var e=t.$refs.uploader.uploader;e.on("fileComplete",function(e,a){t.getList("refresh")}),e.on("complete",function(){t.uploading=!1,0!=t.tableDataUploadFailed.length&&(t.dialogUploadFailed=!0)}),e.on("fileError",function(e,a,i,o){var n=a.name,r=JSON.parse(i).error;if(t.tableDataUploadFailed.push({name:n,reason:r}),"ObjectNameExists"==!JSON.parse(i).error){var s=a.name,l=a.uploader.opts.query.serverPath,c=w.join(l,s).replace("\\","/");t.tmpFileDelete(c)}}),e.on("fileAdded",function(e,a){t.uploading=!0}),e.on("filesAdded",function(e,a,i){t.uploading=!0}),e.on("fileRemoved",function(a){var i=e.fileList,o=!0;for(var n in i)if(!i[n].error&&1!=i[n]._prevProgress){o=!1;break}if(o&&(t.uploading=!1,0!=t.tableDataUploadFailed.length&&(t.dialogUploadFailed=!0)),!a.error&&1!=a._prevProgress){var r=a.name,s=a.uploader.opts.query.serverPath,l=w.join(s,r).replace("\\","/");t.tmpFileDelete(l)}}),e.on("uploadStart",function(){t.uploading=!0}),window.clearInterval(n)}catch(a){console.log(a)}},1)}},sleep:function(t){var e=(new Date).getTime();while((new Date).getTime()-e<t);}}},T=v,x=(a("0bb3"),a("2877")),D=Object(x["a"])(T,u,h,!1,null,"1238bb50",null),C=D.exports,k=a("f923"),_=a.n(k);i["default"].use(_.a),i["default"].config.productionTip=!1,i["default"].use(d.a),i["default"].use(c.a,s.a),i["default"].use(n.a),new i["default"]({render:function(t){return t(C)}}).$mount("#app")},a698:function(t,e,a){"use strict";var i=a("ac63"),o=a.n(i);o.a},ac63:function(t,e,a){},ebad:function(t,e,a){"use strict";var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-container",{staticClass:"container",attrs:{direction:"vertical"}},[a("el-main",[t._t("default")],2)],1)},o=[],n={name:"Layout"},r=n,s=(a("a698"),a("2877")),l=Object(s["a"])(r,i,o,!1,null,"acadd862",null);e["a"]=l.exports},f96f:function(t,e,a){t.exports=a.p+"static/img/folder_icon_b.d6e72493.png"},fa39:function(t,e,a){}});