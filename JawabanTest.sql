select * from desa_kesejahteraan as sjh 
join dim_kabupaten as kbp
on sjh.kabupaten_id=kbp.Kabupaten_ID
;

-- Nomor 1
select kbp.Province_ID, Province_Name, Kabupaten_Name, jumlah_prasejahtera, jumlah_sejahtera1, 
jumlah_sejahtera2, jumlah_sejahtera3, jumlah_sejahtera3plus from desa_kesejahteraan as sjh 
join dim_kabupaten as kbp
on sjh.kabupaten_id=kbp.Kabupaten_ID
join dim_province as prv
on kbp.Province_ID=prv.Province_ID
;

-- Nomor 2
select Province_Name, Kabupaten_Name, jumlah_prasejahtera, jumlah_sejahtera1,
 jumlah_sejahtera2, jumlah_sejahtera3, jumlah_sejahtera3plus from desa_kesejahteraan as sjh 
join dim_kabupaten as kbp
on sjh.kabupaten_id=kbp.Kabupaten_ID
join dim_province as prv
on kbp.Province_ID=prv.Province_ID
where Province_Name = 'JAWA BARAT';

-- Nomor 3
select Province_Name, sum(jumlah) as tenaga_medis from desa_tenagamedis as tng
join dim_kabupaten as kbp
on tng.kabupaten_id=kbp.Kabupaten_ID
join dim_province as prv
on kbp.Province_ID=prv.Province_ID
group by prv.Province_Name;


-- Nomor 4
select Province_Name, Kabupaten_Name, sum(jumlah) as tenaga_medis from desa_tenagamedis as tng
join dim_kabupaten as kbp
on tng.kabupaten_id=kbp.Kabupaten_ID
join dim_province as prv
on kbp.Province_ID=prv.Province_ID
where Province_Name = 'Jawa Timur' and tenaga_medis = 'Bidan'
group by Kabupaten_Name;

-- Nomor 5
select Province_Name, Kabupaten_Name, jumlah_prasejahtera, jumlah_sejahtera1, 
jumlah_sejahtera2, jumlah_sejahtera3, jumlah_sejahtera3plus from desa_kesejahteraan as sjh 
join dim_kabupaten as kbp
on sjh.kabupaten_id=kbp.Kabupaten_ID
join dim_province as prv
on kbp.Province_ID=prv.Province_ID
where Province_Name = 'JAWA TENGAH'
order by jumlah_prasejahtera asc;


-- data bahan

select * from desa_tenagamedis;
select kbp.Province_ID, Province_Name, Kabupaten_Name, jumlah_prasejahtera, jumlah_sejahtera1, jumlah_sejahtera2, jumlah_sejahtera3, jumlah_sejahtera3plus,
tenaga_medis, jumlah from desa_kesejahteraan as sjh 
join dim_kabupaten as kbp
on sjh.kabupaten_id=kbp.Kabupaten_ID
join dim_province as prv
on kbp.Province_ID=prv.Province_ID
join desa_tenagamedis as tng
on tng.kabupaten_id=sjh.kabupaten_id
;
