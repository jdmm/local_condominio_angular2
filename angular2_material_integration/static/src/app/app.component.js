"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var hero_service_1 = require('./hero.service');
var odooCallModel_1 = require('./odooCallModel');
var AppComponent = (function () {
    function AppComponent(heroService) {
        this.heroService = heroService;
        this.title = 'Tour of Heroes';
        // var h = new odooCallModels('siscond_infrastructure.tower',1);
    }
    AppComponent.prototype.onSelect = function (hero) {
        this.selectedHero = hero;
    };
    AppComponent.prototype.getHeroes = function () {
        var _this = this;
        this.heroService.getHeroes().then(function (heroes) { return _this.heroes = heroes; });
    };
    AppComponent.prototype.nameSearch = function (modelName, idModel) {
        var _this = this;
        this.odooCall = new odooCallModel_1.odoocallService();
        this.resNameSearch = [];
        this.odooCall.nameSearch(modelName, idModel).then(function (res) { return _this.resNameSearch = res; });
    };
    AppComponent.prototype.searchRead = function (modelName, domain, fields) {
        var _this = this;
        if (domain === void 0) { domain = null; }
        if (fields === void 0) { fields = null; }
        this.odooCall = new odooCallModel_1.odoocallService();
        this.resSearchRead = [];
        this.odooCall.searchRead(modelName, domain, fields).then(function (res) { return _this.resSearchRead = res; });
    };
    AppComponent.prototype.Call = function (modelName, methodName, args) {
        var _this = this;
        if (args === void 0) { args = null; }
        this.odooCall = new odooCallModel_1.odoocallService();
        this.resCall = [];
        this.odooCall.Call(modelName, methodName, args).then(function (res) { return _this.resCall = res; });
    };
    AppComponent.prototype.ngOnInit = function () {
        this.getHeroes();
        this.nameSearch('siscond_infrastructure.tower', 1);
        this.searchRead('siscond_infrastructure.tower', [['infrastructure_id', '=', 1]], ['name', 'infrastructure_id']);
        // this.Call('siscond_infrastructure.tower','create',[{name:'torre 3',
        //                                                     infrastructure_id:1,
        //                                                     }]);
    };
    AppComponent = __decorate([
        core_1.Component({
            selector: 'my-app',
            template: "\n    <md-toolbar color=\"primary\">\n      Angular Material 2 App\n    </md-toolbar>\n    \n    <div style=\"padding: 7px\">\n      <button md-button>Basic Button</button>\n      <button md-raised-button>Raised Button</button>\n    \n      <md-slide-toggle>Slide Toggle</md-slide-toggle>\n    </div>\n    <h1>{{title}}</h1>\n    <h2>My Heroes</h2>\n\t<md-list class=\"heroes\">\n\t  <md-list-item *ngFor=\"let hero of heroes\" (click)=\"onSelect(hero)\"\n\t  [class.selected]=\"hero === selectedHero\">\n\t  <span class=\"badge\">{{hero.id}}</span> {{hero.name}}\n\t  </md-list-item>\n\t</md-list>\n\t<md-list class=\"heroes\">\n\t<md-list-item *ngFor=\"let model of resNameSearch\">\n\t  <span class=\"badge\">{{model[0]}}</span> {{model[1]}}\n\t  </md-list-item>\n\t</md-list>\n\t<md-list class=\"heroes\">\n\t<md-list-item *ngFor=\"let model of resSearchRead\">\n\t  <span class=\"badge\">{{model.id}}</span> {{model.name}}\n\t  </md-list-item>\n\t</md-list>\n\t<my-hero-detail [hero]=\"selectedHero\"></my-hero-detail>\n\t\n\t<!--<my-odoo-rpc></my-odoo-rpc>-->\n    ",
            styles: ["\n   /*.selected {*/\n    /*background-color: #CFD8DC !important;*/\n/*color: white;*/\n  /*}*/\n  .heroes {\n    margin: 0 0 2em 0;\n    list-style-type: none;\n    padding: 0;\n    width: 15em;\n  }\n  .heroes li {\n    cursor: pointer;\n    position: relative;\n    left: 0;\n    background-color: #EEE;\n    margin: .5em;\n    padding: .3em 0;\n    height: 1.6em;\n    border-radius: 4px;\n  }\n  .heroes li.selected:hover {\n    background-color: #BBD8DC !important;\n    color: white;\n  }\n  .heroes li:hover {\n    color: #607D8B;\n    background-color: #DDD;\n    left: .1em;\n  }\n  .heroes .text {\n    position: relative;\n    top: -3px;\n  }\n  .heroes .badge {\n    display: inline-block;\n    font-size: small;\n    color: white;\n    padding: 0.8em 0.7em 0 0.7em;\n    background-color: #607D8B;\n    line-height: 1em;\n    position: relative;\n    left: -1px;\n    top: -4px;\n    height: 1.8em;\n    margin-right: .8em;\n    border-radius: 4px 0 0 4px;\n  }\n"],
            providers: [
                hero_service_1.HeroService,
                odooCallModel_1.odoocallService
            ]
        }), 
        __metadata('design:paramtypes', [hero_service_1.HeroService])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map