'use strict';

require("core-js/modules/web.dom-collections.iterator.js");

const sentences = [{
  subject: 'JavaScript',
  verb: 'is',
  object: 'great'
}, {
  subject: 'Elephants',
  verb: 'are',
  object: 'large'
}];

function say(_ref) {
  let {
    subject,
    verb,
    object
  } = _ref;
  console.log("".concat(subject, " ").concat(verb, " ").concat(object));
}

for (let s of sentences) {
  say(s);
}