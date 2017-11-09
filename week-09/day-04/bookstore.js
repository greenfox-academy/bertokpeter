'use strict';

const express = require('express');
const app = express();
const mysql = require('mysql');

app.use('/assets', express.static('./assets'));
app.use(express.json());

const conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'bookstore'
});

conn.connect(function(err){
    if(err){
        console.log("Error connecting to Db");
        return;
    } else {
        console.log("Connection established");
    }
});

app.get('/', function(req,res){
    res.sendFile(__dirname + '/index.html');
});

app.get('/list', function(req, res){
    conn.query('SELECT book_name FROM book_mast;', function(err, rows){
        if(err) {
            console.log(err.toString());
        }
        console.log("Data received from Db:\n");
        let htmlString = '<ul>';
        rows.forEach(function(row) {
            htmlString = htmlString + '<li>' + row.book_name + '</li>';
        });
        htmlString = htmlString + '</ul>';
        res.send(htmlString)
    });
});

let selector = `SELECT book_name, aut_name, cate_descrip, pub_name, book_price
FROM book_mast
INNER JOIN author ON book_mast.aut_id = author.aut_id 
INNER JOIN category ON book_mast.cate_id = category.cate_id 
INNER JOIN publisher ON book_mast.pub_id = publisher.pub_id`;

app.get('/all', function(req, res){
    let selectorConditions = queryParser(req.query);
    console.log(selector + selectorConditions);
    conn.query(selector + selectorConditions, function(err, rows){
        if(err) {
            console.log(err.toString());
        }
        let htmlString = '<table>';
        rows.forEach(function(row) {
            htmlString += '<tr><td>' + row.book_name + '</td><td>' + row.aut_name + '</td><td>' + row.cate_descrip + '</td><td>' + row.pub_name + '</td><td>' + row.book_price + '</td></tr>';
        });
        htmlString = htmlString + '</table>';
        res.send(htmlString)
    });
});

function queryParser(query){
    let queryString = '';
    if (query.length !== 0){
        queryString += ' WHERE ';
        if (query.category) {
            queryString += 'cate_descrip = "' + query.category + '" AND ';
        }
        if (query.publisher) {
            queryString += 'pub_name = "' + query.publisher + '" AND ';
        }
        if (query.plt) {
            queryString += 'book_price < ' + query.plt + ' AND ';
        }
        if (query.pgt) {
            queryString += 'book_price > ' + query.pgt + ' AND ';
        }
    }
    queryString = queryString.slice(0,-5);
    queryString += ';';
    return queryString;
}

app.listen(3000);