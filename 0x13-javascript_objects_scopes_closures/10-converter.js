#!/usr/bin/node

exports.converter = function (base) {
  function convert (cambio) {
    return cambio.toString(base);
  }
  return convert;
};
