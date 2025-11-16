### Well hello there!
<!DOCTYPE html>
<html lang="am">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>የቀበሌ ሙሉ መረጃ ስርዓት</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        :root {
            --primary: #2b6cb0;
            --secondary: #38a169;
            --accent: #ed8936;
            --danger: #e53e3e;
            --warning: #d69e2e;
            --light: #f7fafc;
            --dark: #2d3748;
            --gray: #718096;
        }

        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        /* ሄደር */
        header {
            background: white;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            text-align: center;
        }

        h1 {
            color: var(--dark);
            font-size: 2.2em;
            margin-bottom: 10px;
        }

        .amharic-title {
            color: var(--primary);
            font-size: 1.5em;
            margin-bottom: 20px;
        }

        /* ማስተናገያ */
        .navigation {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .nav-btn {
            padding: 15px 25px;
            border: none;
            border-radius: 10px;
            background: white;
            color: var(--dark);
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }

        .nav-btn:hover, .nav-btn.active {
            background: var(--primary);
            color: white;
            transform: translateY(-3px);
        }

        /* ስታትስ */
        .stats-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .stat-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
        }

        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .total-residents .stat-number { color: var(--primary); }
        .total-houses .stat-number { color: var(--secondary); }
        .total-business .stat-number { color: var(--accent); }
        .total-services .stat-number { color: var(--warning); }

        .stat-label {
            color: var(--gray);
            font-size: 1.1em;
        }

        /* የማስገቢያ ክፍሎች */
        .section {
            background: white;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            display: none;
        }

        .section.active {
            display: block;
            animation: fadeIn 0.5s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .section-header {
            display: flex;
            justify-content: between;
            align-items: center;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 2px solid #e2e8f0;
        }

        .section-title {
            font-size: 1.8em;
            color: var(--dark);
        }

        /* ፎርም ንድፎች */
        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 25px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
        }

        label {
            margin-bottom: 8px;
            font-weight: 600;
            color: var(--dark);
        }

        input, select, textarea {
            padding: 15px;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }

        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: var(--primary);
        }

        textarea {
            resize: vertical;
            min-height: 100px;
        }

        .btn {
            padding: 15px 30px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background: #2c5282;
            transform: translateY(-2px);
        }

        .btn-success {
            background: var(--secondary);
            color: white;
        }

        .btn-success:hover {
            background: #2f855a;
            transform: translateY(-2px);
        }

        .btn-outline {
            background: transparent;
            border: 2px solid var(--primary);
            color: var(--primary);
        }

        .btn-outline:hover {
            background: var(--primary);
            color: white;
        }

        /* ሰንጠረዦች */
        .table-container {
            overflow-x: auto;
            margin-top: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }

        th {
            background: var(--primary);
            color: white;
            font-weight: 600;
        }

        tr:hover {
            background: var(--light);
        }

        .action-buttons {
            display: flex;
            gap: 8px;
        }

        .btn-sm {
            padding: 8px 15px;
            font-size: 14px;
        }

        /* ማሳወቂያ */
        .alert {
            padding: 15px;
            border-radius: 10px;
            margin: 15px 0;
            display: none;
        }

        .alert-success {
            background: #c6f6d5;
            color: #276749;
            border: 1px solid #9ae6b4;
        }

        .alert-error {
            background: #fed7d7;
            color: #c53030;
            border: 1px solid #feb2b2;
        }

        /* የቤት ካርድ */
        .houses-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .house-card {
            background: var(--light);
            border-radius: 15px;
            padding: 20px;
            border-left: 5px solid var(--primary);
            transition: all 0.3s ease;
        }

        .house-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .house-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .house-title {
            font-size: 1.2em;
            font-weight: 600;
            color: var(--dark);
        }

        .house-status {
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: 600;
        }

        .status-occupied {
            background: #c6f6d5;
            color: #276749;
        }

        .status-vacant {
            background: #fed7d7;
            color: #c53030;
        }

        .house-details {
            color: var(--gray);
            margin-bottom: 15px;
        }

        /* የንግድ ካርድ */
        .business-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .business-card {
            background: white;
            border-radius: 15px;
            padding: 20px;
            border-left: 5px solid var(--accent);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .business-card:hover {
            transform: translateY(-3px);
        }

        .business-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .business-title {
            font-size: 1.2em;
            font-weight: 600;
            color: var(--dark);
        }

        .business-type {
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: 600;
            background: #feebc8;
            color: #dd6b20;
        }

        /* ሪፖርት ካርድ */
        .reports-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .report-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .report-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }

        .report-icon {
            font-size: 3em;
            margin-bottom: 15px;
        }

        .report-title {
            font-size: 1.3em;
            font-weight: 600;
            color: var(--dark);
            margin-bottom: 10px;
        }

        .report-description {
            color: var(--gray);
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Kebele Information System</h1>
            <div class="amharic-title">የቀበሌ ሙሉ መረጃ ስርዓት</div>
            <p>ሁሉንም የቀበሌ መረጃዎች በአንድ ስርዓት ለማስተዳደር</p>
        </header>

        <!-- ስታትስ -->
        <div class="stats-container">
            <div class="stat-card total-residents">
                <div class="stat-number" id="totalResidents">0</div>
                <div class="stat-label">ጠቅላላ ነዋሪዎች</div>
            </div>
            <div class="stat-card total-houses">
                <div class="stat-number" id="totalHouses">0</div>
                <div class="stat-label">ጠቅላላ ቤቶች</div>
            </div>
            <div class="stat-card total-business">
                <div class="stat-number" id="totalBusiness">0</div>
                <div class="stat-label">የንግድ መዋቅሮች</div>
            </div>
            <div class="stat-card total-services">
                <div class="stat-number" id="totalServices">0</div>
                <div class="stat-label">የአገልግሎት መጠየቂያዎች</div>
            </div>
        </div>

        <!-- ማስተናገያ -->
        <div class="navigation">
            <button class="nav-btn active" onclick="showSection('residents')">👥 ነዋሪዎች</button>
            <button class="nav-btn" onclick="showSection('houses')">🏠 ቤቶች</button>
            <button class="nav-btn" onclick="showSection('business')">🏪 ንግድ</button>
            <button class="nav-btn" onclick="showSection('services')">🔧 አገልግሎቶች</button>
            <button class="nav-btn" onclick="showSection('reports')">📊 ሪፖርቶች</button>
        </div>

        <!-- ነዋሪዎች ክፍል -->
        <section id="residents" class="section active">
            <div class="section-header">
                <h2 class="section-title">ነዋሪዎች አስተዳደር</h2>
                <button class="btn btn-primary" onclick="showResidentForm()">➕ አዲስ ነዋሪ</button>
            </div>

            <div class="form-grid" id="residentForm" style="display: none;">
                <div class="form-group">
                    <label for="residentName">ሙሉ ስም</label>
                    <input type="text" id="residentName" placeholder="ሙሉ ስም" required>
                </div>
                <div class="form-group">
                    <label for="residentAge">ዕድሜ</label>
                    <input type="number" id="residentAge" placeholder="ዕድሜ" required>
                </div>
                <div class="form-group">
                    <label for="residentGender">ጾታ</label>
                    <select id="residentGender" required>
                        <option value="">ምረጥ</option>
                        <option value="male">ወንድ</option>
                        <option value="female">ሴት</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="residentPhone">ስልክ</label>
                    <input type="tel" id="residentPhone" placeholder="+251 ..." required>
                </div>
                <div class="form-group">
                    <label for="residentHouse">የቤት ቁጥር</label>
                    <input type="text" id="residentHouse" placeholder="ቤት ቁጥር" required>
                </div>
                <div class="form-group">
                    <label for="residentId">የመታወቂያ ቁጥር</label>
                    <input type="text" id="residentId" placeholder="መታወቂያ ቁጥር" required>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <label for="residentAddress">አድራሻ</label>
                    <textarea id="residentAddress" placeholder="ዝርዝር አድራሻ"></textarea>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <button class="btn btn-success" onclick="addResident()">💾 ነዋሪ አስገባ</button>
                    <button class="btn btn-outline" onclick="hideResidentForm()">❌ አቋርጥ</button>
                </div>
            </div>

            <div class="table-container">
                <table id="residentsTable">
                    <thead>
                        <tr>
                            <th>ስም</th>
                            <th>ዕድሜ</th>
                            <th>ጾታ</th>
                            <th>ስልክ</th>
                            <th>የቤት ቁጥር</th>
                            <th>ድርጊቶች</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- ነዋሪዎች በጃቫስክሪፕት ይጨመራሉ -->
                    </tbody>
                </table>
            </div>
        </section>

        <!-- ቤቶች ክፍል -->
        <section id="houses" class="section">
            <div class="section-header">
                <h2 class="section-title">ቤቶች አስተዳደር</h2>
                <button class="btn btn-primary" onclick="showHouseForm()">➕ አዲስ ቤት</button>
            </div>

            <div class="form-grid" id="houseForm" style="display: none;">
                <div class="form-group">
                    <label for="houseNumber">የቤት ቁጥር</label>
                    <input type="text" id="houseNumber" placeholder="ቤት ቁጥር" required>
                </div>
                <div class="form-group">
                    <label for="houseOwner">የባለቤት ስም</label>
                    <input type="text" id="houseOwner" placeholder="ባለቤት ስም" required>
                </div>
                <div class="form-group">
                    <label for="houseType">የቤት አይነት</label>
                    <select id="houseType" required>
                        <option value="">ምረጥ</option>
                        <option value="private">ግል</option>
                        <option value="rental">ለኪራይ</option>
                        <option value="commercial">ንግድ</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="houseRooms">የክፍሎች ብዛት</label>
                    <input type="number" id="houseRooms" placeholder="ክፍሎች ብዛት" required>
                </div>
                <div class="form-group">
                    <label for="houseStatus">ሁኔታ</label>
                    <select id="houseStatus" required>
                        <option value="">ምረጥ</option>
                        <option value="occupied">ተከራይ አለ</option>
                        <option value="vacant">ባዶ</option>
                    </select>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <label for="houseAddress">አድራሻ</label>
                    <textarea id="houseAddress" placeholder="ዝርዝር አድራሻ"></textarea>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <button class="btn btn-success" onclick="addHouse()">💾 ቤት አስገባ</button>
                    <button class="btn btn-outline" onclick="hideHouseForm()">❌ አቋርጥ</button>
                </div>
            </div>

            <div class="houses-grid" id="housesGrid">
                <!-- ቤቶች በጃቫስክሪፕት ይጨመራሉ -->
            </div>
        </section>

        <!-- ንግድ ክፍል -->
        <section id="business" class="section">
            <div class="section-header">
                <h2 class="section-title">የንግድ መዋቅሮች</h2>
                <button class="btn btn-primary" onclick="showBusinessForm()">➕ አዲስ ንግድ</button>
            </div>

            <div class="form-grid" id="businessForm" style="display: none;">
                <div class="form-group">
                    <label for="businessName">የንግድ ስም</label>
                    <input type="text" id="businessName" placeholder="ንግድ ስም" required>
                </div>
                <div class="form-group">
                    <label for="businessOwner">የባለቤት ስም</label>
                    <input type="text" id="businessOwner" placeholder="ባለቤት ስም" required>
                </div>
                <div class="form-group">
                    <label for="businessType">የንግድ አይነት</label>
                    <select id="businessType" required>
                        <option value="">ምረጥ</option>
                        <option value="shop">የግብይት ማእከል</option>
                        <option value="restaurant">ምግብ ቤት</option>
                        <option value="service">አገልግሎት</option>
                        <option value="other">ሌላ</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="businessPhone">ስልክ</label>
                    <input type="tel" id="businessPhone" placeholder="+251 ..." required>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <label for="businessAddress">አድራሻ</label>
                    <textarea id="businessAddress" placeholder="የንግድ አድራሻ"></textarea>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <button class="btn btn-success" onclick="addBusiness()">💾 ንግድ አስገባ</button>
                    <button class="btn btn-outline" onclick="hideBusinessForm()">❌ አቋርጥ</button>
                </div>
            </div>

            <div class="business-grid" id="businessGrid">
                <!-- ንግዶች በጃቫስክሪፕት ይጨመራሉ -->
            </div>
        </section>

        <!-- አገልግሎቶች ክፍል -->
        <section id="services" class="section">
            <div class="section-header">
                <h2 class="section-title">አገልግሎት መጠየቂያዎች</h2>
                <button class="btn btn-primary" onclick="showServiceForm()">➕ አዲስ ጥያቄ</button>
            </div>

            <div class="form-grid" id="serviceForm" style="display: none;">
                <div class="form-group">
                    <label for="serviceHouse">የቤት ቁጥር</label>
                    <input type="text" id="serviceHouse" placeholder="ቤት ቁጥር" required>
                </div>
                <div class="form-group">
                    <label for="serviceType">የአገልግሎት አይነት</label>
                    <select id="serviceType" required>
                        <option value="">ምረጥ</option>
                        <option value="water">ውሃ</option>
                        <option value="electricity">ኤሌትሪክ</option>
                        <option value="waste">ቆሻሻ</option>
                        <option value="sanitation">ጽዳት</option>
                        <option value="other">ሌላ</option>
                    </select>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <label for="serviceDescription">የችግር መግለጫ</label>
                    <textarea id="serviceDescription" placeholder="ችግሩን ይግለጹ..."></textarea>
                </div>
                <div class="form-group" style="grid-column: 1 / -1;">
                    <button class="btn btn-success" onclick="addService()">💾 ጥያቄ አስገባ</button>
                    <button class="btn btn-outline" onclick="hideServiceForm()">❌ አቋርጥ</button>
                </div>
            </div>

            <div class="table-container">
                <table id="servicesTable">
                    <thead>
                        <tr>
                            <th>የቤት ቁጥር</th>
                            <th>የአገልግሎት አይነት</th>
                            <th>መግለጫ</th>
                            <th>ቀን</th>
                            <th>ሁኔታ</th>
                            <th>ድርጊቶች</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- አገልግሎቶች በጃቫስክሪፕት ይጨመራሉ -->
                    </tbody>
                </table>
            </div>
        </section>

        <!-- ሪፖርቶች ክፍል -->
        <section id="reports" class="section">
            <div class="section-header">
                <h2 class="section-title">ሪፖርቶች እና ስታትስቲክስ</h2>
            </div>

            <div class="reports-grid">
                <div class="report-card" onclick="generateResidentReport()">
                    <div class="report-icon">👥</div>
                    <div class="report-title">የነዋሪዎች ሪፖርት</div>
                    <div class="report-description">የተመዘገቡ ነዋሪዎች ዝርዝር እና ስታትስቲክስ</div>
                </div>

                <div class="report-card" onclick="generateHouseReport()">
                    <div class="report-icon">🏠</div>
                    <div class="report-title">የቤቶች ሪፖርት</div>
                    <div class="report-description">የቤቶች ሁኔታ እና የተከራዩ ሪፖርት</div>
                </div>

                <div class="report-card" onclick="generateBusinessReport()">
                    <div class="report-icon">🏪</div>
                    <div class="report-title">የንግድ ሪፖርት</div>
                    <div class="report-description">የንግድ መዋቅሮች ዝርዝር እና ስታትስቲክስ</div>
                </div>

                <div class="report-card" onclick="generateServiceReport()">
                    <div class="report-icon">🔧</div>
                    <div class="report-title">የአገልግሎት ሪፖርት</div>
                    <div class="report-description">የአገልግሎት መጠየቂያዎች እና ሁኔታ</div>
                </div>
            </div>

            <div id="reportOutput" style="margin-top: 30px; display: none;">
                <!-- ሪፖርት ውጤት በጃቫስክሪፕት ይጨመራል -->
            </div>
        </section>

        <!-- ማሳወቂያ -->
        <div class="alert alert-success" id="successAlert" style="display: none;">
            ✅ መረጃው በትክክል ተመዝግቧል!
        </div>
    </div>

    <script>
        // የውሂብ ማከማቻ
        let kebeleData = JSON.parse(localStorage.getItem('kebeleData')) || {
            residents: [],
            houses: [],
            businesses: [],
            services: []
        };

        // ክፍል ማሳየት
        function showSection(sectionId) {
            // ሁሉንም ክፍሎች ደብቅ
            document.querySelectorAll('.section').forEach(section => {
                section.classList.remove('active');
            });

            // ሁሉንም አዝራሮች ነቅል
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });

            // የተመረጠውን ክፍል አሳይ
            document.getElementById(sectionId).classList.add('active');
            
            // የተመረጠውን አዝራር አንቁል
            event.target.classList.add('active');

            // ስታትስ አዘምን
            updateStats();
        }

        // ስታትስ ማዘመን
        function updateStats() {
            document.getElementById('totalResidents').textContent = kebeleData.residents.length;
            document.getElementById('totalHouses').textContent = kebeleData.houses.length;
            document.getElementById('totalBusiness').textContent = kebeleData.businesses.length;
            document.getElementById('totalServices').textContent = kebeleData.services.length;
        }

        // ነዋሪ ፎርም ማሳየት/ማደብቅ
        function showResidentForm() {
            document.getElementById('residentForm').style.display = 'grid';
        }

        function hideResidentForm() {
            document.getElementById('residentForm').style.display = 'none';
            document.getElementById('residentForm').reset();
        }

        // ነዋሪ መጨመር
        function addResident() {
            const resident = {
                id: Date.now(),
                name: document.getElementById('residentName').value,
                age: document.getElementById('residentAge').value,
                gender: document.getElementById('residentGender').value,
                phone: document.getElementById('residentPhone').value,
                house: document.getElementById('residentHouse').value,
                idNumber: document.getElementById('residentId').value,
                address: document.getElementById('residentAddress').value,
                date: new Date().toLocaleDateString()
            };

            kebeleData.residents.push(resident);
            localStorage.setItem('kebeleData', JSON.stringify(kebeleData));

            showAlert();
            hideResidentForm();
            displayResidents();
            updateStats();
        }

        // ነዋሪዎችን ማሳየት
        function displayResidents() {
            const tbody = document.querySelector('#residentsTable tbody');
            tbody.innerHTML = '';

            kebeleData.residents.forEach(resident => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${resident.name}</td>
                    <td>${resident.age}</td>
                    <td>${resident.gender === 'male' ? 'ወንድ' : 'ሴት'}</td>
                    <td>${resident.phone}</td>
                    <td>${resident.house}</td>
                    <td class="action-buttons">
                        <button class="btn btn-outline btn-sm" onclick="editResident(${resident.id})">✏️</button>
                        <button class="btn btn-outline btn-sm" onclick="deleteResident(${resident.id})" style="border-color: var(--danger); color: var(--danger);">🗑️</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        // ቤት ፎርም ማሳየት/ማደብቅ
        function showHouseForm() {
            document.getElementById('houseForm').style.display = 'grid';
        }

        function hideHouseForm() {
            document.getElementById('houseForm').style.display = 'none';
            document.getElementById('houseForm').reset();
        }

        // ቤት መጨመር
        function addHouse() {
            const house = {
                id: Date.now(),
                number: document.getElementById('houseNumber').value,
                owner: document.getElementById('houseOwner').value,
                type: document.getElementById('houseType').value,
                rooms: document.getElementById('houseRooms').value,
                status: document.getElementById('houseStatus').value,
                address: document.getElementById('houseAddress').value,
                date: new Date().toLocaleDateString()
            };

            kebeleData.houses.push(house);
            localStorage.setItem('kebeleData', JSON.stringify(kebeleData));

            showAlert();
            hideHouseForm();
            displayHouses();
            updateStats();
        }

        // ቤቶችን ማሳየት
        function displayHouses() {
            const grid = document.getElementById('housesGrid');
            grid.innerHTML = '';

            kebeleData.houses.forEach(house => {
                const typeText = 
                    house.type === 'private' ? 'ግል' :
                    house.type === 'rental' ? 'ለኪራይ' : 'ንግድ';

                const statusText = house.status === 'occupied' ? 'ተከራይ አለ' : 'ባዶ';
                const statusClass = house.status === 'occupied' ? 'status-occupied' : 'status-vacant';

                const card = document.createElement('div');
                card.className = 'house-card';
                card.innerHTML = `
                    <div class="house-header">
                        <div class="house-title">ቤት ${house.number}</div>
                        <span class="house-status ${statusClass}">${statusText}</span>
                    </div>
                    <div class="house-details">
                        <div>👤 ባለቤት: ${house.owner}</div>
                        <div>🏠 አይነት: ${typeText}</div>
                        <div>🚪 ክፍሎች: ${house.rooms}</div>
                        <div>📍 ${house.address}</div>
                    </div>
                    <div class="action-buttons">
                        <button class="btn btn-outline btn-sm" onclick="editHouse(${house.id})">✏️</button>
                        <button class="btn btn-outline btn-sm" onclick="deleteHouse(${house.id})" style="border-color: var(--danger); color: var(--danger);">🗑️</button>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        // ንግድ ፎርም ማሳየት/ማደብቅ
        function showBusinessForm() {
            document.getElementById('businessForm').style.display = 'grid';
        }

        function hideBusinessForm() {
            document.getElementById('businessForm').style.display = 'none';
            document.getElementById('businessForm').reset();
        }

        // ንግድ መጨመር
        function addBusiness() {
            const business = {
                id: Date.now(),
                name: document.getElementById('businessName').value,
                owner: document.getElementById('businessOwner').value,
                type: document.getElementById('businessType').value,
                phone: document.getElementById('businessPhone').value,
                address: document.getElementById('businessAddress').value,
                date: new Date().toLocaleDateString()
            };

            kebeleData.businesses.push(business);
            localStorage.setItem('kebeleData', JSON.stringify(kebeleData));

            showAlert();
            hideBusinessForm();
            displayBusinesses();
            updateStats();
        }

        // ንግዶችን ማሳየት
        function displayBusinesses() {
            const grid = document.getElementById('businessGrid');
            grid.innerHTML = '';

            kebeleData.businesses.forEach(business => {
                const typeText = 
                    business.type === 'shop' ? 'የግብይት ማእከል' :
                    business.type === 'restaurant' ? 'ምግብ ቤት' :
                    business.type === 'service' ? 'አገልግሎት' : 'ሌላ';

                const card = document.createElement('div');
                card.className = 'business-card';
                card.innerHTML = `
                    <div class="business-header">
                        <div class="business-title">${business.name}</div>
                        <span class="business-type">${typeText}</span>
                    </div>
                    <div class="house-details">
                        <div>👤 ባለቤት: ${business.owner}</div>
                        <div>📞 ስልክ: ${business.phone}</div>
                        <div>📍 ${business.address}</div>
                    </div>
                    <div class="action-buttons">
                        <button class="btn btn-outline btn-sm" onclick="editBusiness(${business.id})">✏️</button>
                        <button class="btn btn-outline btn-sm" onclick="deleteBusiness(${business.id})" style="border-color: var(--danger); color: var(--danger);">🗑️</button>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        // አገልግሎት ፎርም ማሳየት/ማደብቅ
        function showServiceForm() {
            document.getElementById('serviceForm').style.display = 'grid';
        }

        function hideServiceForm() {
            document.getElementById('serviceForm').style.display = 'none';
            document.getElementById('serviceForm').reset();
        }

        // አገልግሎት መጨመር
        function addService() {
            const service = {
                id: Date.now(),
                house: document.getElementById('serviceHouse').value,
                type: document.getElementById('serviceType').value,
                description: document.getElementById('serviceDescription').value,
                status: 'pending',
                date: new Date().toLocaleDateString()
            };

            kebeleData.services.push(service);
            localStorage.setItem('kebeleData', JSON.stringify(kebeleData));

            showAlert();
            hideServiceForm();
            displayServices();
            updateStats();
        }

        // አገልግሎቶችን ማሳየት
        function displayServices() {
            const tbody = document.querySelector('#servicesTable tbody');
            tbody.innerHTML = '';

            kebeleData.services.forEach(service => {
                const typeText = 
                    service.type === 'water' ? 'ውሃ' :
                    service.type === 'electricity' ? 'ኤሌትሪክ' :
                    service.type === 'waste' ? 'ቆሻሻ' :
                    service.type === 'sanitation' ? 'ጽዳት' : 'ሌላ';

                const statusText = service.status === 'pending' ? 'በመጠባበቅ ላይ' : 'ተጠናቅቋል';
                const statusColor = service.status === 'pending' ? 'orange' : 'green';

                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${service.house}</td>
                    <td>${typeText}</td>
                    <td>${service.description}</td>
                    <td>${service.date}</td>
                    <td style="color: ${statusColor}; font-weight: bold;">${statusText}</td>
                    <td class="action-buttons">
                        <button class="btn btn-success btn-sm" onclick="completeService(${service.id})">✅</button>
                        <button class="btn btn-outline btn-sm" onclick="deleteService(${service.id})" style="border-color: var(--danger); color: var(--danger);">🗑️</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        // አገልግሎት ማጠናቀቅ
        function completeService(serviceId) {
            const service = kebeleData.services.find(s => s.id === serviceId);
            if (service) {
                service.status = 'completed';
                localStorage.setItem('kebeleData', JSON.stringify(kebeleData));
                displayServices();
                alert('አገልግሎቱ እንደተጠናቀቀ ተመዝግቧል!');
            }
        }

        // ማሳወቂያ ማሳየት
        function showAlert() {
            const alert = document.getElementById('successAlert');
            alert.style.display = 'block';
            setTimeout(() => {
                alert.style.display = 'none';
            }, 3000);
        }

        // ሪፖርት ማመንጨት ተግባራት
        function generateResidentReport() {
            const output = document.getElementById('reportOutput');
            output.style.display = 'block';
            output.innerHTML = `
                <div class="section" style="display: block;">
                    <h3>👥 የነዋሪዎች ሪፖርት</h3>
                    <p><strong>ጠቅላላ ነዋሪዎች:</strong> ${kebeleData.residents.length}</p>
                    <p><strong>ወንዶች:</strong> ${kebeleData.residents.filter(r => r.gender === 'male').length}</p>
                    <p><strong>ሴቶች:</strong> ${kebeleData.residents.filter(r => r.gender === 'female').length}</p>
                    <button class="btn btn-primary" onclick="printReport()">🖨️ ሪፖርት አትም</button>
                </div>
            `;
        }

        function generateHouseReport() {
            const output = document.getElementById('reportOutput');
            output.style.display = 'block';
            output.innerHTML = `
                <div class="section" style="display: block;">
                    <h3>🏠 የቤቶች ሪፖርት</h3>
                    <p><strong>ጠቅላላ ቤቶች:</strong> ${kebeleData.houses.length}</p>
                    <p><strong>ተከራይ ያላቸው:</strong> ${kebeleData.houses.filter(h => h.status === 'occupied').length}</p>
                    <p><strong>ባዶ ቤቶች:</strong> ${kebeleData.houses.filter(h => h.status === 'vacant').length}</p>
                    <button class="btn btn-primary" onclick="printReport()">🖨️ ሪፖርት አትም</button>
                </div>
            `;
        }

        function generateBusinessReport() {
            const output = document.getElementById('reportOutput');
            output.style.display = 'block';
            output.innerHTML = `
                <div class="section" style="display: block;">
                    <h3>🏪 የንግድ ሪፖርት</h3>
                    <p><strong>ጠቅላላ ንግዶች:</strong> ${kebeleData.businesses.length}</p>
                    <p><strong>የግብይት ማእከሎች:</strong> ${kebeleData.businesses.filter(b => b.type === 'shop').length}</p>
                    <p><strong>ምግብ ቤቶች:</strong> ${kebeleData.businesses.filter(b => b.type === 'restaurant').length}</p>
                    <button class="btn btn-primary" onclick="printReport()">🖨️ ሪፖርት አትም</button>
                </div>
            `;
        }

        function generateServiceReport() {
            const output = document.getElementById('reportOutput');
            output.style.display = 'block';
            output.innerHTML = `
                <div class="section" style="display: block;">
                    <h3>🔧 የአገልግሎት ሪፖርት</h3>
                    <p><strong>ጠቅላላ ጥያቄዎች:</strong> ${kebeleData.services.length}</p>
                    <p><strong>በመጠባበቅ ላይ:</strong> ${kebeleData.services.filter(s => s.status === 'pending').length}</p>
                    <p><strong>ተጠናቅቀዋል:</strong> ${kebeleData.services.filter(s => s.status === 'completed').length}</p>
                    <button class="btn btn-primary" onclick="printReport()">🖨️ ሪፖርት አትም</button>
                </div>
            `;
        }

        function printReport() {
            window.print();
        }

        // መሰረዝ ተግባራት (ለቅንጅት)
        function deleteResident(id) {
            if (confirm('ይህን ነዋሪ ለመሰረዝ እርግጠኛ ነዎት?')) {
                kebeleData.residents = kebeleData.residents.filter(r => r.id !== id);
                localStorage.setItem('kebeleData', JSON.stringify(kebeleData));
                displayResidents();
                updateStats();
            }
        }

        function deleteHouse(id) {
            if (confirm('ይህን ቤት ለመሰረዝ እርግጠኛ ነዎት?')) {
                kebeleData.houses = kebeleData.houses.filter(h => h.id !== id);
                localStorage.setItem('kebeleData', JSON.stringify(kebeleData));
                displayHouses();
                updateStats();
            }
        }

        function deleteBusiness(id) {
            if (confirm('ይህን ንግድ ለመሰረዝ እርግጠኛ ነዎት?')) {
                kebeleData.businesses = kebeleData.businesses.filter(b => b.id !== id);
                localStorage.setItem('kebeleData', JSON.stringify(kebeleData));
                displayBusinesses();
                updateStats();
            }
        }

        function deleteService(id) {
            if (confirm('ይህን ጥያቄ ለመሰረዝ እርግጠኛ ነዎት?')) {
                kebeleData.services = kebeleData.services.filter(s => s.id !== id);
                localStorage.setItem('kebeleData', JSON.stringify(kebeleData));
                displayServices();
                updateStats();
            }
        }

        // አርትዕ ተግባራት (ለቅንጅት)
        function editResident(id) {
            alert('አርትዕ ባህሪ በቅጂት ላይ ነው። በቅርቡ ይጨምራል!');
        }

        function editHouse(id) {
            alert('አርትዕ ባህሪ በቅጂት ላይ ነው። በቅርቡ ይጨምራል!');
        }

        function editBusiness(id) {
            alert('አርትዕ ባህሪ በቅጂት ላይ ነው። በቅርቡ ይጨምራል!');
        }

        // ገጹ ሲጫን ውሂቦችን አሳይ
        document.addEventListener('DOMContentLoaded', () => {
            updateStats();
            displayResidents();
            displayHouses();
            displayBusinesses();
            displayServices();
        });
    </script>
</body>
</html>

This repository is meant to provide an example for *forking* a repository on GitHub.

Creating a *fork* is producing a personal copy of someone else's project. Forks act as a sort of bridge between the original repository and your personal copy. You can submit *Pull Requests* to help make other people's projects better by offering your changes up to the original project. Forking is at the core of social coding at GitHub.

After forking this repository, you can make some changes to the project, and submit [a Pull Request](https://github.com/octocat/Spoon-Knife/pulls) as practice.

For some more information on how to fork a repository, [check out our guide, "Forking Projects""](http://guides.github.com/overviews/forking/). Thanks! :sparkling_heart:
