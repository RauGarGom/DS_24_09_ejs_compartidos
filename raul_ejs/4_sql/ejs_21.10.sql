/* EJERCICIO 1 */
SELECT *
FROM customers
WHERE Country ='Brazil';

/* EJERCICIO 2 */
SELECT * FROM employees
WHERE Title LIKE '%Sales%';

/* EJERCICIO 3 */
select *
From artists
INNER JOIN albums on albums.ArtistId = artists.ArtistId
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId
WHERE artists.Name = 'AC/DC';

/* Solución de clase */
SELECT *
FROM tracks AS t
INNER JOIN albums AS al ON al.AlbumId = t.AlbumId
INNER JOIN artists AS ar ON ar.ArtistId = al.ArtistId
WHERE ar.Name = 'AC/DC';

/* EJERCICIO 4 */
SELECT concat(firstname,' ',lastname) as nombre_completo, customerid, country from customers
WHERE COUNTRY IS NOT 'USA';

/* Clase */
SELECT firstname || ' ' || lastname as nombre_completo, customerid as id, country as pais
from customers
where country <> 'USA';

/* EJERCICIO 5 */
SELECT concat(firstname, ' ', lastname) AS nombre_completo, 
concat(address,', ',city,', ',state,', ',country) as direccion, 
email FROM employees
WHERE Title LIKE '%Sales%';

/* EJERCICIO 6 */
SELECT DISTINCT billingcountry from invoices;


/* EJERCICIO 7 */
SELECT COUNT(customerid) as num_facturas, State from customers
WHERE country = 'USA'
GROUP BY state
order BY num_facturas DESC;


/* EJERCICIO 8 */
select it.InvoiceId as Factura, count(it.InvoiceLineId) as num_items
FROM invoice_items as it
INNER JOIN invoices as inv on inv.InvoiceId = it.InvoiceId
where inv.InvoiceId = 37
GROUP BY it.invoiceid

/* EJERCICIO 9 */
select artists.Name, count(artists.ArtistId)
From artists
INNER JOIN albums on albums.ArtistId = artists.ArtistId
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId
WHERE artists.Name = 'AC/DC'
GROUP BY artists.Name;

/* EJERCICIO 10 */
SELECT invoiceid, count(invoicelineid) from invoice_items
group by InvoiceId;


/* EJERCICIO 11 */
SELECT count(invoiceid),billingcountry from invoices
group by billingcountry
order by 1 DESC;

/* EJERCICIO 12 */
SELECT count(invoiceid) from invoices
WHERE invoicedate LIKE ('2009%') AND ('2011%');

/* EJERCICIO 13 */
SELECT * from invoices
WHERE invoicedate BETWEEN ('2009-01-01') AND ('2011-12-31');

/* EJERCICIO 14 */
SELECT billingcountry, count(invoiceid) from invoices
WHERE billingcountry IN ('Spain','Brazil')
group by billingcountry;

/* EJERCICIO 15 */
SELECT name from tracks
where name like 'You%'

/*Segunda parte */
/* EJERCICIO 1 */
select concat(cs.FirstName, cs.LastName) as nombre_cliente, inv.invoiceid, inv.invoicedate, inv.BillingCountry
from invoices as inv
INNER JOIN customers as cs on cs.CustomerId = inv.CustomerId

/* EJERCICIO 2 */
select inv.InvoiceId, concat(em.firstname, ' ',em.lastname)  from invoices as inv
INNER JOIN customers AS cs ON inv.CustomerId = cs.CustomerId
inner join employees as em on em.EmployeeId = cs.SupportRepId;

/* EJERCICIO 3 */
select count(inv.InvoiceId) as num_invoices, concat(cs.FirstName, ' ', cs.LastName) as customer_name,cs.country, concat(em.firstname, ' ',em.lastname) AS agent_name from invoices as inv
INNER JOIN customers AS cs ON inv.CustomerId = cs.CustomerId
inner join employees as em on em.EmployeeId = cs.SupportRepId
group by agent_name;

/* EJERCICIO 4 */
select it.invoiceid, tr.Name from invoice_items as it
inner join tracks as tr on tr.TrackId = it.TrackId

/* EJERCICIO 5 */
SELECT tr.Name as track_name, gr.Name as genre, md.Name as media, al.Title as album from tracks as tr
INNER JOIN genres as gr on gr.GenreId = tr.GenreId
inner join media_types as md on md.MediaTypeId = tr.MediaTypeId
inner join albums as al on al.AlbumId = tr.AlbumId

/* EJERCICIO 6 */
SELECT playlistid, count(trackid) from playlist_track
group by playlistid

/* EJERCICIO 7 */
SELECT concat(em.firstname, ' ',em.lastname) as emp_name, SUM(inv.total) from employees as em
INNER join customers as cs on cs.SupportRepId = em.EmployeeId
inner join invoices as inv on inv.CustomerId = cs.CustomerId
GROUP by emp_name

/* EJERCICIO 8 */
SELECT concat(em.firstname, ' ',em.lastname) as emp_name, SUM(inv.total) as total_sum from employees as em
INNER join customers as cs on cs.SupportRepId = em.EmployeeId
inner join invoices as inv on inv.CustomerId = cs.CustomerId
WHERE inv.invoicedate LIKE ('2009%')
GROUP by emp_name
order by 2 desc
LIMIT 1;

/* EJERCICIO 9 */
Select ar.Name as artist, SUM(inv.total) as total_sum from artists as ar
inner JOIN albums as al on al.ArtistId = ar.ArtistId
INNER JOIN tracks as tr on tr.AlbumId = al.AlbumId
INNER JOIN invoice_items as it on it.TrackId = tr.TrackId
inner join invoices as inv on inv.InvoiceId = it.InvoiceId
group by artist
order by 2 DESC
limit 3;

