import { useEffect, useRef, useState } from "react";
import "./App.css";

function App() {
  const time = useRef<string>();
  time.current = Date().toString();

  
  const [value, setValue] = useState<string>();
  const intro = `🏴‍☠️ Hackster Corp.\nShell Version 1.0\nStarted On : ${time.current}\n\nTutorial : type "help" in the terminal and press Enter.\n\nTips : Hackster Team tried to copy most of the linux terminal features.\n\n`;
  const text = useRef<any>();
  const inputblock = useRef<any>();


  
  useEffect(()=>{let i = 0;let intro_inter = setInterval(()=>{if (i < intro.split('').length) {text.current.textContent += intro.split('')[i];i++} else {clearInterval(intro_inter);inputblock.current.classList.remove('hidden')}},50)},[]);

  const handlesub = (e:any) => {if (e) {}}
  return (
    <>
      <pre ref={text}></pre>
      <pre className="row hidden" ref={inputblock}>localuser@Hackster $ <input type="text" className="term-input" value={value} autoFocus={true} onChange={(e:any)=>setValue(e.target.value)} onSubmit={handlesub} ></input></pre>
    </>
  );
}

export default App;
