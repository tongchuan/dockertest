
// window.addEventListener('error',function(...reset){
// 	console.log(reset)
// },false)
// window.onerror=function(message,source,lineno,colno,error){
// 	console.log(message,source,lineno,colno,error)
// }
window.onerror=function(...args){
	console.log('args',args)
}

window.onunhandledrejection=function(event){
	event = event || window.event
	var errorMsg = ""
	var errorStack = ""
	if(typeof event.reason === 'object'){
		errorMsg = event.reason.message;
		errorStack = event.reason.stack;
	}else{

	}
}

window.onload=function(){
  let ziyuan = window.performance.getEntries()
  // console.log(ziyuan)
  let navigationsource = performance.getEntriesByType('navigation')
  // console.log(navigationsource)
  let resourceSource = performance.getEntriesByType('resource')
  // console.log(resourceSource)
  for(var i=0;i<resourceSource.length;i++){
    let name = resourceSource[i].name
    let item = performance.getEntriesByName(name)[0]
    console.log(item)
    console.log(item.toJSON())
  }
}


// performance.mark("Begin");
// let count=1
// while(count<500){
//   count++
//   console.log('log')
// }
// performance.mark("End");
// performance.mark("Begin");
// count=1
// while(count<500){
//   count++
//   console.log('log')
// }
// performance.mark("End");
//   count=1
// while(count<500){
//   count++
//   console.log('log')
// }
// performance.mark("End");



function perf_observer(list, observer) {
  console.log('list, observer',list, observer)
   // Process the "measure" event
   // 处理 "measure" 事件
}
var observer2 = new PerformanceObserver(perf_observer);
observer2.observe({entryTypes: ["measure"]});