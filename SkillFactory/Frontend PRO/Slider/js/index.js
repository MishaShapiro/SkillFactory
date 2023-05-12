const information = [{
	sity: "Rostov-on-Don LCD admiral",
	app_arr: "81 m2",
	rep_time: "3.5 months",
	rep_cost: "Upon request",
	img: "img/image 2.1.png"
},
{
	sity: "Sochi Thieves",
	app_arr: "105 m2",
	rep_time: "4 months",
	rep_cost: "Upon request",
	img: "img/image 2.png"
},
{
	sity: "Rostov-on-Don Patriotic",
	app_arr: "93 m2",
	rep_time: "3 months",
	rep_cost: "Upon request",
	img: "img/image 3.png"
}]

let current_slide = 0;
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
const point1 = document.querySelector(".prev");
const point2 = document.querySelector(".prev"); 
const point3 = document.querySelector(".prev");
const image = document.querySelector(".img");
const content_sity = document.querySelector(".city_text");
const content_app_arr = document.querySelector(".apartment_text");
const content_rep_time = document.querySelector(".repairtime_text");
const content_rep_cost = document.querySelector(".repaircost_text");
const blockinfo = document.querySelectorAll(".blockinfo");
const svg1 = document.querySelector(".svg1");
const svg2 = document.querySelector(".svg2");
const svg3 = document.querySelector(".svg3");
const points = [svg1, svg2, svg3];
const links = document.querySelectorAll(".link_text")

function oppas() {
	for (let i = 0; i < blockinfo.length; i++) {
		blockinfo[i].style.opacity = "0.3"
	}
	setTimeout(deppas, 400)
}

function deppas() {
	for (let i = 0; i < blockinfo.length; i++) {
		blockinfo[i].style.opacity = "1"
	}
}

function uload_all() {
	image.setAttribute("src", information[current_slide].img)
	image.style.rotate = "0deg"
	image.style.scale = "1"
	content_sity.innerText = information[current_slide].sity
	content_app_arr.innerText = information[current_slide].app_arr
	content_rep_time.innerText = information[current_slide].rep_time
	content_rep_cost.innerText = information[current_slide].rep_cost
	for (let i = 0; i <= 2; i++) {
		if (i == current_slide) {
			links[i].style.color = "#E3B873"
			links[i].style.opacity = "1"
			links[i].style.borderBottom = "1px solid #E3B873"
			points[i].style.opacity = "1"
		} else {
			links[i].style.color = "white"
			links[i].style.borderBottom = "0px"
			links[i].style.opacity = "0.3"
			points[i].style.opacity = "0.3"
		}
	}
}

function prev_slide() {
	if (current_slide == 0) {
		current_slide = 2
	} else {
		current_slide -= 1
	}
	image.style.rotate = "200deg"
	image.style.scale = "0.5"
	oppas()
	setTimeout(uload_all, 400)
}

function next_slide() {
	if (current_slide == 2) {
		current_slide = 0
	} else {
		current_slide += 1
	}
	image.style.rotate = "200deg"
	image.style.scale = "0.5"
	oppas()
	setTimeout(uload_all, 400)
}

function slide(num) {
	if (num != current_slide) {
		current_slide = num
		image.style.rotate = "200deg"
		image.style.scale = "0.5"
		oppas()
		setTimeout(uload_all, 400)
	}
}

function slide1() {
	slide(0)
}
function slide2() {
	slide(1)
}
function slide3() {
	slide(2)
}

prev.addEventListener("click", prev_slide)
next.addEventListener("click", next_slide)
links[0].addEventListener("click", slide1)
links[1].addEventListener("click", slide2)
links[2].addEventListener("click", slide3)
