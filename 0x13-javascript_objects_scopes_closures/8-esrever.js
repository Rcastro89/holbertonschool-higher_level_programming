#!/usr/bin/node

exports.esrever = function (list) {
  let pos = list.length - 1;
  const newList = [];
  for (pos; pos >= 0; pos--) {
    newList.push(list[pos]);
  }
  return newList;
};
