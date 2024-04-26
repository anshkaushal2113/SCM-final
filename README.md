# TimeSheet.js Demo
<html>
  <head></head>
    <body>
<div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/timesheet.js/1.0.0/timesheet.min.js"></script>
  <style>
    #timesheet {
      width: 100%;
      max-width: 800px;
      margin: 0 auto;
    }
  </style>
</div>

<div id="timesheet"></div>

<script>
  var data = [
    { start: '2024-04-01', end: '2024-04-04', label: 'Project A' },
    { start: '2024-04-02', end: '2024-04-05', label: 'Project B' },
    { start: '2024-04-05', end: '2024-04-07', label: 'Project C' },
    { start: '2024-04-10', end: '2024-04-15', label: 'Project D' }
    // Add more data as needed
  ];

  var ts = new TimeSheet('timesheet', data, {
    theme: 'default',
    round: false,
    showDates: true,
    labels: {
      off: 'Off',
      on: 'On'
    }
  });

  ts.draw();
</script>
</body>
</html>
