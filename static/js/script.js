import { xType,xRevType } from "./SymType.js";

const sleep = ms => new Promise(r => setTimeout(r, ms));

document.addEventListener("DOMContentLoaded", async () => {
  const mainName = document.querySelector("#P1-D1-H1");
  const root = document.documentElement;
  const changeNameEng = "Hello, I'm Fauzan Rizky";
  const changeNameZh = "哈喽, 我是 法武赞•力泽琪";
  await sleep(1500)
  while(true){
    root.style.setProperty('--P1D1bg', '#FFFFFF')
    xRevType(mainName, "_")
    await sleep(750)
    xType(mainName, changeNameEng, "_")
    await sleep(5000)
    

    root.style.setProperty('--P1D1bg', '#51EEFC')
    xRevType(mainName, "_")
    await sleep(1200)
    xType(mainName, changeNameZh, "_")
    await sleep(5000)
  }
})

window.addEventListener('scroll', () => {
  document.body.style.setProperty('--scroll', window.scrollY / (document.body.offsetHeight - window.innerHeight));
}, false);

console.log("Hello, world!")