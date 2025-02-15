import { useEffect, useRef, useState } from "react";
import "./App.css";
import {WhoAmI} from "./features/Commands";

function App() {
  const time = useRef<string>();
  time.current = Date().toString();

  const [value, setValue] = useState<string>("");
  const intro: string = `🏴‍☠️ Hackster Corp.\nShell Version 1.0\nStarted On : ${time.current}\n\nTutorial : type "help" in the terminal and press Enter.\n\nTips: AutoFocus is "on", when any key is pressed.\n\n`;
  const text = useRef<any>();
  let PS1:string = "localuser@Hackster $"; // dont leave space at the end, it will be preadded
  const inputblock = useRef<any>();
  const input_element = useRef<any>();

  //Initial Typewriter Effect
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

  //Local Function to Print text to Terminal
  function print_to_term(data: string) {
    //Dont add \n to your string, it will be preadded
    text.current.textContent += `\n${data}\n`;
  }

  //Gateway to Execution
  const handlesub = (e: any) => {
    if (e) {
      e.preventDefault();
      print_to_term(`${PS1} ${value}`);
      print_to_term(codecheck(value));
      setValue("");
      console.log(value);
    }
  };

  //Command Checker
  const codecheck:(arg0: string)=>string = (command: string) => {
    //Parsing
    let tokens = command.split(" ");
    let found = false;
    let output = "";
    tokens.forEach((val)=>{while (val.includes(' ')) {val = val.replace(' ',"")}});
    const final_token = tokens.filter((val)=>val.length > 0);
    const help_check = final_token.includes('-h') || final_token.includes('--help');
    const version_check = final_token.includes('--version');

    switch (final_token[0]) {
      case "whoami":
        found = true;
        const value = new WhoAmI();
        if (help_check) {
          output = value.help();
        } else if (version_check) {
          output = `'${value.name}' Module\nVersion ${value.version}`;
        } else {
          output = value.run(final_token);
        }

    }
    return found ? output : `'${final_token[0]}' module not found, Contact Admin.`;
  }


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
