/*
Command Blueprint

class <Command_Name> {
    #secret_variable

    name: string;
    version: number;
    constructor() {
        this.#secret_variable = "Access secret variables";
        this.version = "mandatory";
        this.name = "mandatory , will be used to call";
        this.author = "your name";
        this.public_variable = "Public Variable";
    }

    run(tokens : string[]) { //tokens are passed from terminal after parsing
    //do something

    return "" // or return "error this is not found etc";
    }

    //a mandatory function that returns help
    help() {
    return "this class have these options  -f -fg -g etc etc";
    }
}

    for example and use a command is given
*/


//Export the Command that you make, and Import them in App.tsx
export class WhoAmI {
    name: string;
    version: number;
    constructor() {
        this.name = "whoami";
        this.version = 1.0;
    }
    
    run(tokens: string[]) {
        if (tokens.length > 2) {
            return "options were not needed\nyou are a Loser.";
        }
        return "you are a CTF Player";
    }

    help() {
        return "You know, you are getting an existencial crisis.";
    }

}






