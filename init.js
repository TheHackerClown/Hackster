//Intro Typewriter effect
let intro = `Hackster 🏴‍☠️\nShell Version 1.0\nStarted On: ${new Date()}\nNote: use "help" to explore.\n`;
const myInput = document.getElementById('input');
window.addEventListener('DOMContentLoaded',()=>{
    let i = 1;
    let keypress = 0;
    var intro_intrvl = setInterval(function () {
        window.addEventListener('keydown',(event)=>{keypress++;})
        if (i > intro.length || keypress > 0) {
            clearInterval(intro_intrvl)
            $('#intro').text(intro)
            $('#data').css('display', 'block')
            window.removeEventListener('keydown',(event)=>{keypress++;})
            myInput.focus()

        } else {
            $('#intro').text(intro.slice(0,i++))
        }
    },100);
})

//For Mouseless Interaction
window.addEventListener('keydown', ()=>{myInput.focus()})

function ask(question) {
    return new Promise((resolve) => {
        window.removeEventListener('keydown',focus(myInput))
        var form = document.createElement("form");
        form.action = "/";
        form.method = "post";
        form.id = "user_form";

        var addressDiv = document.createElement("div");
        addressDiv.id = "address";
        addressDiv.textContent = question;
        var inputDiv = document.createElement("div");

        var userInput = document.createElement("input");
        userInput.type = "text";
        userInput.id = "user_input";

        inputDiv.appendChild(userInput);
        form.appendChild(addressDiv);
        form.appendChild(inputDiv);
        var output = document.getElementById('output');
        output.appendChild(form);
        window.addEventListener('keydown',focus(userInput))
        $('#user_form').on('submit', (event)=>{
            event.preventDefault();
            const answr = $('#user_input').val();
            form.remove();
            $('#output').append('\n<a>'+question+' '+answr+'</a>');
            window.removeEventListener('keydown',focus(userInput))
            window.addEventListener('keydown',focus(myInput));
            resolve(answr);
        })
    
    })         
}

//Function to write output
function wrt(data) {
    $('#output').append('\n'+data)
}

// Logic of the Terminal
$('#data').on('submit',async function (event) {
    //Using HTML Form for getting user input
    event.preventDefault();
    window.removeEventListener('keydown',() => {myInput.focus()})

    //Variables
    let found = 0;

    //Input Parsing
    var input = $('#input').val().split(' ');
    input = input.filter(ele => ele != '');

    //Resetting Form
    $('#input').val('');
    $('#output').append('\n<a>User@THC $ '+input.join(' ')+'</a>');
    $('#data').css('display','none');
    console.log(input);
    //Command deciding
    //Checking If Numeric Expression to be evaluated
    try {
        var result = eval(input.join(' '));
        found++;
    } catch(error) {
        //Not an Expression, should be a command
        for (let comm in commands) {
            if (commands[comm].name === input[0] && found == 0) {
                if (input[input.length-1] === '-h') {
                    var result = await commands[comm].help(input);
                    found++;
                    break;
                } else {
                    var result = await commands[comm].result(input);
                    found++;
                    break;
                }
            }
        }
        
    } finally {
        $('#data').css('display','block');
        window.addEventListener('keydown',()=>{myInput.focus()});
        if (found === 0) {
            //Not an Command
            wrt('"'+input.join(' ')+'" is not recognized as an command. Please use "help" to get a list of commands.\nIf you want, you can create "'+input.join(' ')+'" command using command manual given in the git.')
        } else {
            //Writing the output
            wrt(result)
        }
    }
})
