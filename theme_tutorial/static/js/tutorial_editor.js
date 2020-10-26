
 odoo.define('theme_tutorial.web_editor', function (require) {
 "use strict";

    var options = require('web_editor.snippets.options');
    options.registry.snippet_testimonial_options = options.Class.extend({
        console.log("Hello world!");
        start: function () {
            alert("On focus!")
        },
    });
 });