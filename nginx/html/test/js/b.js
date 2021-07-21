

// window.addEventListener('DOMContentLoaded',function(){
// 	console.log('window.DOMContentLoaded')
// })
document.addEventListener('DOMContentLoaded',function(event){
	event = event || window.event
	event.cancelBubble=true
	event.stopPropagation()
	event.preventDefault()
	a = 4
	console.log(args)
	let a =  222
	console.log('document.DOMContentLoaded')
})

