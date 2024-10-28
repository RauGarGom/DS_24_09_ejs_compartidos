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
select artists.ArtistId, artists.Name, count(artists.ArtistId)
From artists
INNER JOIN albums on albums.ArtistId = artists.ArtistId
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId
WHERE artists.Name = 'AC/DC'
GROUP BY artists.ArtistId,artists.Name;

/* EJERCICIO 10 */
SELECT invoiceid, count(invoicelineid) from invoice_items
group by InvoiceId
ORDER BY 2 DESC;

/* Clase */
SELECT invoiceid, SUM(quantity) from invoice_items
group by InvoiceId
ORDER BY 2 DESC;

/* EJERCICIO 11 */
SELECT billingcountry, count(invoiceid) from invoices
group by billingcountry
order by 2 DESC;

/* EJERCICIO 12 */
SELECT count(invoiceid) from invoices
WHERE invoicedate LIKE ('2009%') OR ('2011%');

/* Clase */
SELECT strftime('%Y', invoicedate) AS Año,
COUNT(invoiceid)
From invoices
where año in ('2009','2011')
GROUP BY 1;

/* EJERCICIO 13 */
SELECT * from invoices
WHERE invoicedate BETWEEN ('2009-01-01') AND ('2011-12-31');

/* EJERCICIO 14 */
SELECT billingcountry, count(invoiceid) from invoices
WHERE billingcountry IN ('Spain','Brazil')
group by billingcountry;

/* Ojo, era con los clientes) */
SELECT country,
COUNT(customerid)
FROM customers
WHERE Country in ('Spain','Brazil')
GROUP BY 1; 


/* EJERCICIO 15 */
SELECT name from tracks
where name like 'You%'

/*clase. Con esto cogemos también los que sean en minúscula */
SELECT name from tracks
where LOWER(name) like 'You%'

/*Segunda parte */
/* EJERCICIO 1 */
select concat(cs.FirstName,' ',cs.LastName) as nombre_cliente, inv.invoiceid, inv.invoicedate, inv.BillingCountry
from invoices as inv
INNER JOIN customers as cs on cs.CustomerId = inv.CustomerId
where cs.Country = 'Brazil';

/* EJERCICIO 2 */
select inv.InvoiceId, concat(em.firstname, ' ',em.lastname)  from invoices as inv
INNER JOIN customers AS cs ON inv.CustomerId = cs.CustomerId
inner join employees as em on em.EmployeeId = cs.SupportRepId;

/* EJERCICIO 3 */
select concat(cs.FirstName, ' ', cs.LastName) as customer_name, concat(em.firstname, ' ',em.lastname) AS agent_name,cs.country,count(inv.InvoiceId) as num_invoices from invoices as inv
INNER JOIN customers AS cs ON inv.CustomerId = cs.CustomerId
inner join employees as em on em.EmployeeId = cs.SupportRepId
group by agent_name,customer_name;

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
group by playlistid;

/* Clase */
SELECT pl.PlaylistId, pl.Name, count(pt.trackid) from playlist_track as pt
inner JOIN playlists as pl on pl.PlaylistId = pt.PlaylistId
group by pl.PlaylistId
ORDER BY 3 desc;

/* EJERCICIO 7 */
SELECT em.EmployeeId, concat(em.firstname, ' ',em.lastname) as emp_name, SUM(inv.total) as total, count(inv.InvoiceId) as num_invoices, count(DISTINCT cs.CustomerId) as num_customers from employees as em
INNER join customers as cs on cs.SupportRepId = em.EmployeeId
INNER join invoices as inv on inv.CustomerId = cs.CustomerId
GROUP by emp_name
order by total desc;

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

