import { Component } from '@angular/core';

@Component({
    selector: 'my-app',
    template:  require('./app.component.html')
})
export class AppComponent {

    constructor(){
        console.log("Angular! is here :)")
    }
}
