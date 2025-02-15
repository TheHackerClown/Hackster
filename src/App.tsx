import { useEffect, useRef, useState } from "react";
import "./App.css";

function App() {
  const time = useRef<string>();
  time.current = Date().toString();

  const [value, setValue] = useState<string>();
  const intro = `🏴‍☠️ Hackster Corp.\nShell Version 1.0\nStarted On : ${time.current}\n\nTutorial : type "help" in the terminal and press Enter.\n\nTips : Hackster Team tried to copy most of the linux terminal features.\n\nTips: AutoFocus is "on",when any key is pressed.\n`;
  const text = useRef<any>();
  let PS1 = "localuser@Hackster $"; // dont leave space at the end, it will be preadded
  const inputblock = useRef<any>();
  const input_element = useRef<any>();

  useEffect(() => {
    let i = 0;
    let intro_inter = setInterval(() => {
      if (i < intro.split("").length) {
        text.current.textContent += intro.split("")[i];
        i++;
      } else {
        clearInterval(intro_inter);
        inputblock.current.classList.remove("hidden");
        window.addEventListener("keydown", () => {
          input_element.current.focus();
        });
      }
    }, 50);
  }, []);

  function print_to_term(data: string) {
    //Dont add \n to your string, it will be preadded
    text.current.textContent += `\n${data}\n`;
  }

  const handlesub = (e: any) => {
    if (e) {
      e.preventDefault();
      print_to_term(`${PS1} ${value}`);
      setValue("");
      console.log(value);
    }
  };
  return (
    <>
      <pre ref={text}></pre>
      <form className="row hidden" ref={inputblock} onSubmit={handlesub}>
        <pre className="row">
          {`${PS1} `}
          <input
            type="text"
            className="term-input"
            value={value}
            autoFocus={true}
            onChange={(e: any) => setValue(e.target.value)}
            ref={input_element}
          ></input>
        </pre>
      </form>
    </>
  );
}

export default App;
