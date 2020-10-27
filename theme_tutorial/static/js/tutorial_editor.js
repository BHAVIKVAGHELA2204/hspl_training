/*
odoo.define('theme_tutorial.test_editor', function (require) {
 "use strict";

    var options = require('web_editor.snippets.options');
    options.registry.snippet_testimonial_options = options.Class.extend({
    console.log(">>>>>>>>>");
        onFocus: function () {
            this._super.apply(this, arguments);
            console.log(">>>>>>>>>", this);
            alert("On focus!")
        },
    });
 });*/
 odoo.define(function (require) {
    var options = require('web_editor.snippets.options');
    options.registry.snippet_testimonial_options = options.Class.extend({
        onFocus: function () {
            alert("On focus!")
        },
    });
});
