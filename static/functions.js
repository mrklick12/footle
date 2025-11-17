function formatDate(date)
{
    // 2025-11-22T12:30:00Z
    let time = date.slice(11,16);
    let day = date.slice(8,10);
    let month = date.slice(5,7);

    let formated_date = day + "/" + month + "   " + time;

    return formated_date;
}



