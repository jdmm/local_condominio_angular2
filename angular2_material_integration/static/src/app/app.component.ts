import { Component } from '@angular/core';
import { Hero } from './hero';
import { HeroService } from './hero.service';
import { OnInit } from '@angular/core';
import { Http, ConnectionBackend, RequestOptions } from "@angular/http";
import { odoocallService } from './odooCallModel';

@Component({
  selector: 'my-app',
  template: `
    <md-toolbar color="primary">
      Angular Material 2 App
    </md-toolbar>
    
    <div style="padding: 7px">
      <button md-button>Basic Button</button>
      <button md-raised-button>Raised Button</button>
    
      <md-slide-toggle>Slide Toggle</md-slide-toggle>
    </div>
    <h1>{{title}}</h1>
    <h2>My Heroes</h2>
	<md-list class="heroes">
	  <md-list-item *ngFor="let hero of heroes" (click)="onSelect(hero)"
	  [class.selected]="hero === selectedHero">
	  <span class="badge">{{hero.id}}</span> {{hero.name}}
	  </md-list-item>
	</md-list>
	<md-list class="heroes">
	<md-list-item *ngFor="let model of resNameSearch">
	  <span class="badge">{{model[0]}}</span> {{model[1]}}
	  </md-list-item>
	</md-list>
	<md-list class="heroes">
	<md-list-item *ngFor="let model of resSearchRead">
	  <span class="badge">{{model.id}}</span> {{model.name}}
	  </md-list-item>
	</md-list>
	<my-hero-detail [hero]="selectedHero"></my-hero-detail>
	
	<!--<my-odoo-rpc></my-odoo-rpc>-->
    `,
   styles: [`
   /*.selected {*/
    /*background-color: #CFD8DC !important;*/
/*color: white;*/
  /*}*/
  .heroes {
    margin: 0 0 2em 0;
    list-style-type: none;
    padding: 0;
    width: 15em;
  }
  .heroes li {
    cursor: pointer;
    position: relative;
    left: 0;
    background-color: #EEE;
    margin: .5em;
    padding: .3em 0;
    height: 1.6em;
    border-radius: 4px;
  }
  .heroes li.selected:hover {
    background-color: #BBD8DC !important;
    color: white;
  }
  .heroes li:hover {
    color: #607D8B;
    background-color: #DDD;
    left: .1em;
  }
  .heroes .text {
    position: relative;
    top: -3px;
  }
  .heroes .badge {
    display: inline-block;
    font-size: small;
    color: white;
    padding: 0.8em 0.7em 0 0.7em;
    background-color: #607D8B;
    line-height: 1em;
    position: relative;
    left: -1px;
    top: -4px;
    height: 1.8em;
    margin-right: .8em;
    border-radius: 4px 0 0 4px;
  }
`],


        providers: [
            HeroService,
            odoocallService
            ]


})
export class AppComponent implements OnInit {
    title = 'Tour of Heroes';
    heroes : Hero[];
    resNameSearch: any[];
    resSearchRead: any[];
    resCall: any[];
    odooCall : any ;
    selectedHero: Hero;
    onSelect(hero: Hero): void {
        this.selectedHero = hero;
    }


    constructor(private heroService: HeroService) {
        // var h = new odooCallModels('siscond_infrastructure.tower',1);
    }

     getHeroes(): void {
        this.heroService.getHeroes().then(heroes => this.heroes = heroes);
     }

     nameSearch(modelName: string, idModel: number): void {
         this.odooCall = new odoocallService()
         this.resNameSearch = [];
         this.odooCall.nameSearch(modelName,idModel).then(res => this.resNameSearch = res)
     }

     searchRead(modelName: string, domain: [string, string, any][]= null, fields: string[] = null):void{
         this.odooCall = new odoocallService()
         this.resSearchRead = [];
         this.odooCall.searchRead(modelName,domain,fields).then(res => this.resSearchRead = res)
     }

     Call(modelName: string, methodName: string, args: any[] = null):void{
         this.odooCall = new odoocallService()
         this.resCall = [];
         this.odooCall.Call(modelName,methodName,args).then(res => this.resCall = res)
     }

    ngOnInit(): void {
        this.getHeroes();
        this.nameSearch('siscond_infrastructure.tower',1);
        this.searchRead('siscond_infrastructure.tower',[['infrastructure_id','=',1]],['name','infrastructure_id']);
        // this.Call('siscond_infrastructure.tower','create',[{name:'torre 3',
        //                                                     infrastructure_id:1,
        //                                                     }]);
  }

}







