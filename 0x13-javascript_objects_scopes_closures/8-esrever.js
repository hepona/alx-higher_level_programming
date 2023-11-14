#!/usr/bin/node
exports.esrever = function (list) {
  const listCp = [];
  for (let i = 0; i < list.length; i++) {
    listCp[i] = list[(list.length - 1) - i];
  }
  return listCp;
};
