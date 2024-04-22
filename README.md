## PRODUCT FEATURES

- Pacient’s anylisis based in TCM methods and results with symptoms, syndromes, meridians states, warning signs, meaning of pulse and thongs exams.
- Previous exams based in CSV files.
- 208 prescriptions based in each diagnosed as suggested automatic outputs, possible to erase or editing and even consults the several methods of TCM (shu-points, mu-points, specified shens and 13 texts and diagrams of use as consult support).
- Native integrated diagnoses in TCM as current’s World Health Organization new ICD-11 (new worldwide catalog).
- Possible of analysis based in cun-guan-chi types, 28 types of pulses, thongs color, dimensions, moviments, warmith and humidity states, as also skin, pain, eyes analysis and Huang di’s Nei jing methods of cunkou-renyng differencial methods.
- Detection of suggestion of recommendations of mu, sun si miao’s ghosts’ points, shu and chronoacupuncture based in shi tian gan’s local time method, liu xie, ni’s pathologies, star and windows of heaven points, luo, ho, xi, yuan, muxi and all wonderful vases indications as possible automatic marks.
- Multi-selection of treatments and editable accuponts automatic prescriptions and running of smart algorithm that prevents dozens of needles, adapting for best mean marge.
- Suggestion of Chinease and Japanese extrameridian’s uses and action base and location alike.
- Use of IDs for privacity of pacients name and data.
- Local data storage allowing mobility for clouding porpouses.


## ABOUT LOGGING ACCESS NUMBERS

TAO IS PROGRAMMED FOR MANDATORY USE OF CPF FOR ID LOG, THERE IS A SHREWD ALGORITHM FOR IT'S USE AND NOT USED IN USA, FOR TESTING USE THE LINK IN FOOTER OF ITEM

- What is a Brazilian CPF?
A CPF is an individual taxpayer identification number given to people living in Brazil, both native Brazilians and resident aliens, who pay taxes. The CPF number is an identification number of Brazilian citizens emitted by the Brazilian Ministry of Revenue, which is called "Ministério da Fazenda".
- What does CPF stand for?
CPF stands for Cadastro de Pessoas Físicas (Natural Persons Register). Native Brazilians can request a CPF at any time in their lives - parents will often apply on behalf of their children when they are newborns, as CPFs are vital to living in Brazil and it’s best to obtain one sooner rather than later.
- A CPF is 11 digits long, comprised of nine base digits, and two digits at the end that are the result of an arithmetic operation on the first nine numbers, meaning any typing mistakes will lead to an invalid number. Here is an example of a CPF: 231.002.999-00.
- The CPF is comprised of a base of 9 digits and 2 check digits. It is usually written like '231.002.999-00' so as to be more human-readable.

This module provides test_cpf for checking that a CPF number is correct. Here a correct CPF number means
it is 11 digits long
it satisfies the two check equations mentioned below
Before checking, any non-digit letter is stripped, making it easy to test formatted entries like '231.002.999-00' and entries with extra blanks like ' 999.221.222-00 '.

test_cpf
test_cpf('999.444.333-55') # incorrect CPF, returns 0
test_cpf(' 263.946.533-30 ') # is ok, returns 1
test_cpf('888') # nope, returns undef
Tests whether a CPF number is correct. Before testing, any non-digit character is stripped. Then it is expected to be 11 digits long and to satisfy two check equations which validate the last two check digits. See "THE CHECK EQUATIONS".
The policy to get rid of '.' and '-' is very liberal. It indeeds discards anything that is not a digit (0, 1, ..., 9) or letter. That is handy for discarding spaces as well
test_cpf(' 263.946.533-30 ') # is ok, returns 1
But extraneous inputs like '#333%444*2.3+2-00' are also accepted. If you are worried about this kind of input, just check against a regex:
warn "bad CPF: only digits (11) expected"
  unless ($cpf =~ /^\d{11}$/);
warn "bad CPF: does not match mask '___.___.___-__'"
  unless ($cpf =~ /^\d{3}\.\d{3}\.\d{3}-\d{2}$/);
NOTE. Integer numbers like 9999811299 (or 99_998_112_99) with fewer than 11 digits will be normalized (eg. to "09999811299") before testing.
canon_cpf
canon_cpf(99); # returns '00000000099'
canon_cpf('999.999.999-99'); # returns '99999999999'
Brings a candidate for a CPF number to a canonical form. In case, the argument is an integer, it is formatted to at least eleven digits. Otherwise, it is stripped of any non-alphanumeric characters and returned as it is.
format_cpf
format_cpf('00000000000'); # returns '000.000.000-00'
Formats its input into '000.000.000-00' mask. First, the argument is canon'ed and then dots and hyphen are added to the first 11 digits of the result.
parse_cpf
($base, $dv) = parse_cpf($cpf);
$hashref = parse_cpf('999.222.111-00'); # { base => '999222111', dv => '00' }
Splits a candidate for CPF number into base and check digits (dv - dígitos de verificação). It canon's the argument before splitting it into 9- and 2-digits parts. In a list context, returns a two-element list with the base and the check digits. In a scalar context, returns a hash ref with keys 'base' and 'dv' and associated values.
random_cpf
$rand_cpf = random_cpf($valid);
$correct_cpf = random_cpf();
$cpf = random_cpf(1); # also a correct CPF
$bad_cpf = random_cpf(0); # an incorrect CPF
Generates a random CPF. If $valid is omitted or 1, it is guaranteed to be correct. If $valid is 0, it is guaranteed to be incorrect. This function is intented for mass test. (Use it wisely.)
The implementation is simple: just generate a 9-digits random number, hopefully with a uniform distribution and then compute the check digits. If $valid==0, the check digits are computed not to satisfy the check equations.


THE CHECK EQUATIONS
A correct CPF number has two check digits which are computed from the base 9 first digits. Consider the CPF number written as 11 digits
c[1] c[2] c[3] c[4] c[5] c[6] c[7] c[8] c[9] dv[1] dv[2]
To check whether a CPF is correct or not, it has to satisfy the check equations:
c[1]*10+c[2]*9+c[3]*8+c[4]*7+c[5]*6+
        c[6]*5+c[7]*4+c[8]*3+c[9]*2+dv[1] = 0 (mod 11) or
                                          = 1 (mod 11) (if dv[1]=0)
and
c[2]*10+c[3]*9+c[4]*8+c[5]*7+c[6]*6+
        c[7]*5+c[8]*4+c[9]*3+dv[1]*2+dv[2] = 0 (mod 11) or
                                           = 1 (mod 11) (if dv[2]=0)
                                           
HYPERLINK FOR GENERATION OR VALID NUMBER'S CHECK:
https://www.4devs.com.br/gerador_de_cpf


## UPDATE'S VERSIONS

### 1.0.0 : OPERATIONAL BETA
### 1.0.1 : INITIAL FUNCTIONAL
### 1.0.2 : ADDED DICTIONARY OF CHOICE TERMS
### 1.0.3 : TRIGGERED PATHOLOGICAL PULSE AS OUTPUT
### 1.0.4 : NORMAL PULSE PATTERNS ALGORITHM IN PATHOLOGICAL (AUTOMATION)
### 1.1.0 : FULLY INTEGRAL ALGORITHM OF NORMAL AND PATHOLOGICAL PULSE
### 1.1.2 : ADDED LANGUAGE ANALYSIS OUTPUT AND PULSE DATA PLOTTING GENERATION
### 1.1.3 : ADDED PRESCRIPTION AND CHOICE TREE LOGIC WITH REUSE OF ITEMS AND PASSWORD FOR FORMATTING
### 1.1.4 : INTEGRATE DATABASE WITH PRESCRIPTION MODULE VIA CSV
### 1.1.5 : CID11 INTEGRATION WITH SYSTEM
### 1.1.6 : MODULATION OF BIN/BIAO RESCUE STEPS, DATACENTER REDESIGN
### 1.1.7 : FIX SAVE CRASH IN CASE OF NOT PRESCRIBING AND VIEW EXAM RESULTS, RELEASED CODE TO SAVE
### 2.0.1 : ADD QUESTIONNAIRE FOR MU/XU/LUO/YUAN/HUI/WINDOW/STAR/SU SI MIAO/ANCIENT SHU/DORSAL SHU/EXTRAORDINARY DAIS POINT ALGORITHM
### 2.0.2 : SCREEN ADJUSTMENT DURING CYCLES
### 2.0.3 : NEW DIAGNOSTIC DATA ANALYSIS ALGORITHM WITH NEW ERROR CAPTURE SET, DIAGNOSTIC DICT CORRECTION
### 2.0.4 : ADDITION OF TECHNICAL APPENDIX IN PRESCRIPTION
### 2.1.0 : MODULATION OF ALGORITHMS FOR DATA INTERSECTION TO FORMULATE DEFINITIVE DIAGNOSIS AND OTHER ADJUSTMENTS FOR THE PATCH
### 2.1.1 : COLLISION CORRECTION BY NEW ANALYSIS ALGORITHM
### 2.1.2 : CORRECTION OF GENERAL ERRORS THAT PREVENTED THE CORRECT OPERATION OF THE PROGRAM (IDENTERS AND CHOICE TREES IN LOOP, AS WELL AS INSERTION OF DATABASE CHECKERS), INSERTION OF SLEEP IN ERRORS THAT WERE DELETED IN CLS(SLEEP) COMMAND NOT BEING LOCATED (FOR BETTER AESTHETICS KEPT CLS WITH SLEEP IN ERRORS TO BE READ), NOTIFICATIONS IN MODULES THAT USE DATABASE IN CASE OF INACTIVE FILE (DATA CONTINGENCY)
### 2.1.3 : SET ANALYSIS TO CHECK EMPTY MEMORY, BLOCKING COLLISIONS OF DATA FROM DIFFERENT PATIENTS, SIMPLIFIED DATA PLOT OBLITERATION (STABLE VERSION)
### 2.1.4 : ADDITION OF TRIPLE HEATER ANALYSIS AND 4 HEAT-WIND LEVELS VIA AUTOMATIC ALGORITHM
### 2.1.5 : ADDITION OF ICD11 TO THE TERMS OF TREATMENT AUTOMATICALLY
### 2.1.6 : PATCH TO FILTER UNRESTRICTED UNIFIED FIELD AUTOMATICALLY, UNIFYING FIELDS THAT REQUIRED SEQUENCE IN THE PHYSICAL EXAMINATION NOT ALWAYS FOLLOWED
### 2.2.0 : ADDITION OF VOLTAGE FOR APPROXIMATION CALCULATION OR DEFINITION IN DIAGNOSTIC ALGORITHM A.I.
### 2.2.1 : ADJUSTMENT OF ALGORITHM CORRECTION FOR CASES OF ANTAGONISMS, PATCH OF MULTI-INSERTION OF SELECTION TABLE WITH ADDITION OF ERASING, VERIFICATION AND CORRECTION OF POINTS IN CASE OF DIPLICITY WITH DIFFERENT METHODS, ADDITION OF TRIPLE HEATER ANALYSIS WITH LOCATION DEFINITION AND ADDITION OF CID, MEMORY DELETION AFTER ALGORITHM TERMINATION, EDITING OF SELECTION OF POINTS INDIVIDUALLY (UNSTABLE)
### 2.2.2 : DEBUGGING ERRORS, STABILIZING SCRIPTS, AND REINTRODUCING ELECTIVE PLOTTING WITH NEW DATA FROM THE NEW ALGORITHM, ALLOWING BETTER USE
### 2.2.3 : TENSOR ALGORITHM CORRECTION (UNION AND INTERSESSION WERE NOT PERFORMED DUE TO LIST/SET DIFFERENCE AND ANOTHER STRING FOR ALGORITHM POST-ADJUSTMENT WAS UNUSABLE)
### 2.2.4 : INSERTION OF SYNDROME PROTOCOL BY ANALYSIS OF PATHOLOGICAL PULSE COMBINATIONS VIA UNSTRUCTURED NEURAL NETWORK
### 2.3.5 : WARNINGS IN CALCULATION CORRECTIONS
### 2.3.6 : PATTERN ANALYSIS FOR BIN/BIAO AND PATTERN DESCRIPTION WITH FOOD SUGGESTIONS
### 2.3.7 : ADDITION OF CLINICAL HISTORY, PAIN ANALYSIS AND TACTILE SENSES
### 2.3.8 : DEBUGGING TAGS ERROR AND SAVING, REDUCING GLOBALS
### 2.3.9 : PULSE REVIEW ### CORRECTION PATCH FOR DETECTED ERRORS
### 3.0 : REVISION OF GLOBAL STANDARDS AND TRADE-OFFS BY FUNCTIONS
### 3.1 : HEAT/WIND LIU XIE CORRECTION WITH ALL SIGNALS UNDER ANALYSIS
### 3.2 : POCKET EDITION
### 3.3 : BUG FIX THAT PREVENTED SYMPTOMS FROM APPEARING CORRUPTED CODE
### 3.4.0 : COLD/HEAT AND AT DIAGNOSTICS NOW GO STRAIGHT IN WITH CERTAINTY DIAGNOSTICS
### A1 : TONGUE ALGORITHM CORRECTION, MORE FLUID. BACKUP USED FOR SEVERE INDENTATION ERROR, UNDER DOWNGRADE AND PATCH
### A2 : MODULE COMPATIBILITY AND STABILIZATION
### A3 : PRESCRIPTION SEPARATION FOR APPLICATION CLASSES
### A4 : ORDERING OF CLASSES DUE TO COLLIDERS IN LOOPS AND LIST COMPREHENSIONS
### A5 : EXTENDED LOOPS FOR CALCULATIONS
### A6 : CRUDE CALCULATION OF STITCHES AND NUMBER OF NEEDLES
### A7 : TOTALITARIAN CALCULATION OF NEEDLES VIA UNIT POINT ANALYSIS, BUG FIX OF MULTIPLE DX ENTRIES IN TREATMENT TARGETS (MAKING APPEAR INSTEAD OF NAME ONLY NUMBER IF MULTIPLE DATA) ### STABLE
### A8 : IMPROVEMENT OF LISTS AND EXPOSURES OF PRINTS AND TRANSLATION OF ICD-11 APPLIED IN TCM
### A9 : ADDED DESCRIPTION OF SYMPTOMS OF WIND-HEAT LIU XIE SYNDROMES AND CORRECTION OF INDEXING OF THEM, ADDED COMPLEXION ANALYSIS IN RESULTS
### BETA-1 : DELIMITATION AFTER ANALYSIS OF NEW ATTEMPT TO LOCATE BIN
### BETA-2 : UPDATE OF ICD-11 LIST TO PORTUGUESE
### BETA-3 : ADDITION OF TIMEZONE IN BRASILIA AND PROGRAMMED SHU POINTS BY CHRONOACUPUNCTURE
### BETA-4 : PATCH TESTS
### GAMMA-1: IMPLEMENTED TREATMENT PROTOCOLS GUIDED BY POST-EXPOSURE SELECTION
### GAMMA-2 : DEAD-END PATCH LOOP FLOW CORRECTION VIA ONE-WAY MODULE
### GAMMA-3 : DATA FLOW AUTOMATION IMPLEMENTATION TESTS (PROTOCOL PRESCRIPTIONS
### DELTA-1: IMPLEMENTATION OF 74 NEW AUTOMATED PROTOCOLS
### DELTA-2 : FIXED PATHWAY DEFRAGMENTED BY NEW ADDITIONS
### DELTA-3 : FIX SEVERE SYMPTOM TABLE DISPOSITION FUNCTION FLOW ERROR
### DELTA-4 : CORRECTION OF DISAPPEARANCE ERROR OF SPECIFIC SYMPTOMS OF WIND-COLD AND WIND-HEAT SYNDROMES
### DELTA-5 : FIX CODE DEGENERATION IN INDENT FORMATTING, WITH CODE CRASH
### DELTA-6 : ADDITION OF A SEASON FOR PUNCTURE TYPES ACCORDING TO CLASSICAL CHINESE MEDICINE
### DELTA-7 : ADDITION OF WEATHER CONDITION FOR FULL COLD TREATMENT
### TAO 1.0.0 : BINARY BUILDS FOR EXPORT AND WITHOUT ACCESS VIA GOOGLE FOR COPYRIGHT
### TAO 1.0.1 : IMPROVED CLIMATE ANALYSIS AND WARN_PUN FOR ONLINE TIME/CLIMATE REQUESTS AND TECHNIQUE PRESCRIPTION
### TAO 1.0.2 : ADDITION OF PREGNANCY TEST, RENYING'S TEST, PHYSIQUE EXAMINATION OF NOSTRIL, EYE, BETWEEN EYEBROWS, FOREARM EXAMINATION AND GENERATION OF TREATMENT VARIABLES, AIMING AT THERAPY BY TYPE OF PUNCTURE (BONE, MUSCLE, TENDON, CANAL) ACCORDING TO PROTOCOL
### TAO 1.0.3 : CORRECTION ALGORITHM VIA STATION FOR RENYING TEST (ACCORDING TO YELLOW EMPEROR)
### TAO 1.0.4 : ADDED HDA TEXTUAL ANALYSIS FOR DATA COLLECTION VIA WU XING GENERAL TABLE, DESIGN IMPROVEMENT, AND FLOW LAYOUT
### TAO 1.0.5: DUE TO THE POINT DISPLAY NOT BEING SEPARATED BY MERIDIANS AND DUE TO AN ERROR THAT ALLOWED DUPLICITY OF POINTS IN SEDATION AND TONING, UNIFICATION ADJUSTMENT OF DOUBLE Acronyms IN SEDATION/TONIFICATION, MOXA AND LATERALITY CATEGORIES ALLOWING SPLIT [ 1:] BE IN VERIFICATION SET ACCORDING TO TYPE OF APPLICATION, HOWEVER REQUIRED PATCH TO CORRECTION PRESCRIPTION INSERTION FLOWS, CORRECTION OF INSERTION AUTOMATION FOR NEW PARAMETERS. WITHDRAWAL OF WARN_PUN MARKING TAGS (IN LETTERS), BECOMING SENSE ON DISPLAY AND ALREADY IMPLEMENTED
### TAO 1.0.6: CODING ERROR COMPATIBLE WITH ADJUSTMENT IN 1.0.5, DOWNGRADE BEING PERFORMED AND NEW UNIFIED CODING MAINTAINED FOR DOUBLES OF LETTER IN PRESCRIPTIONS AND ARRANGEMENT OF POINTS
### TAO 1.0.7: ADJUSTMENT OF DICT AND CID DIRECTORIES WITH PERFECT DISPOSITION FUNCTIONS AND IMPROVED DOWNGRADE STABILITY
### TAO 1.0.8: ADDITION OF ACUPUNCTURE TAILORED TO PATHOLOGIES OF NON-ORIENTAL MEDICINE
### TAO 2.0.0: UPDATE OF ALL EXTRA POINTS (UNIFICATION OF LITERARY NOMENCLATURES WITH LOCATION IN THE PRESCRIPTION AND INTEGRATION OF SEARCH AND NOTES)
### TAO 2.0.1: POINT COUNT ADJUSTMENT FOR NEW EXTRAS WITH CORRECTION VIA DIFFERENTIAL SETS WITHOUT REQUIRING NUMERAL FLUCTUATIONS
### TAO 2.0.2: INSERT BPM ANALYSIS FOR COMPATIBLE PULSE ALGORITHM
### TAO 2.0.3: INDEX CORRECTION BY NAME-LOCATION SEARCH AND USE OF PANDAS TO DISPLAY PULSOLOGY AND SANJIAO
### TAO 2.0.5: INSERTION OF THE ENTIRE MERIDIAN ERASE COMMAND, ADJUSTMENT OF THE EXPLANATION TEXT ARRANGEMENT OF PAINS AND MERIDIAN LOCATIONS, ADJUSTMENT OF SEPARATION IN WORD COMPOSITION, CHANGE OF EXPLANATORY TEXT ABOUT PUNCTURES RECOMMENDED BY STATION AND INSERT OF SUMMARY TEXT TO DIAGNOSTIC BRIEFING
### TAO 2.0.6: ADDITION OF FUNCTION DELIMITING MORE POINTS BEYOND THE BLADDER FOR NOTIFICATION OF POINTS ON THE BACK (MAKING PATIENTS NOT TO WASTE TIME APPLYING ON THE BACK WITH DIFFERENT POINTS)
### TAO 2.1.0: IMPROVEMENT OF THE PRESCRIBED POINT CHOICE ALGORITHM WITH CALCULATED RESTRICTION FOR FEWER NEEDLES THE MORE DIAGNOSIS IS ADDED ### NOT ALLOWING 200 NEEDLES FOR 5 DIAGNOSES, FOR EXAMPLE; ADDITION OF PULSOLOGY SPECIFICATION AND DESCRIPTIONS OF SPECIFIC SYMPTOMS BY LOCATION OF PULSE TYPES AND LOCATIONS (YELLOW EMPEROR CLASSICAL MEDICINE DESCRIPTION, VERY SPECIFIC SYMPTOMS NOT GENERALIST)
### TAO 2.1.1: CORRECTION OF 7 BUGS DUE TO UPDATE, STABILIZATION OF ITERATIVE FUNCTIONS, ADJUSTMENT OF PROGRAM REPORTS AND FINAL EXPOSITORY AND SUMMARY REPORT
### TAO 2.1.2: STRUCTURAL AND TEXTUAL CORRECTION WITH REINTRODUCTION OF INFORMATION ARCHIVING WITH DATA INDEXING, STILL IN OPERATIONALIZATION
### TAO 2.1.3: ADDITION OF AGE CALCULATION AND DATA COMPLEMENTATION FOR EXPORT TO NÄIVE-BAYES ALGORITHM
### TAO 2.2: IMPLEMENTATION OF DATABASE FILES FOR AI ANALYSIS AND PATIENT CONSULTATION VIA .CSV IN LOCAL USE
### TAO 2.3: CORRECTIONAL PATCH DUE TO LOSS OF COHERENCE WITH WITHDRAWAL OF GLOBALS AFFECTING DEF METRO AND DEF ONLY (DOWNGRADE FOLLOWING METRO AND ONLY VIA 2.1.1) WITHOUT FINDING ERROR AND WITHOUT RUNNING STABLE VERSION
### TAP 2.4: DATABASE IMPLEMENTATION
### TAO 2.5: ADDING CPF AS A QUERY IDENTIFIER (INCLUDING VERIFICATION ALGORITHM) AND ADDING JING JIN ANALYSIS
### TAO 2.6: STABLE AND CORRECTED VERSION, FOR BACKUP
### TAO 2.7: CPF IMPLEMENTATION FOR DATABASE CONSULTATION, SELF-COMPLETING PATIENT DATA AND SHOWING PREVIOUS TREATMENT
### TAO 2.8: NEW TREE OF CHOICES ALGORITHM IN GENERATION, DOMINANCE, COUNTER-DOMINANCE AND NON-GENERATION CYCLES
### TAO 2.9: ADDING SEARCH TO ZIP CODE AND ADDRESS REGISTRATION, IN ADDITION TO SHOWING LAST APPOINTMENT HISTORY AND AUTOMATICALLY COMPLETED ADDRESSES AND IDENTITIES
### TAO 3.0: VERIFICATION AND CORRECTION OF MEMORY ALLOCATED FOR NEW FUNCTIONS, REDONE MEMORY DEF() AFTER PROGRAM END
### TAO 3.1: INTERNET VERIFICATION WITH ACCESS TO ASTRONOMY AND WEATHER FORECAST PLATFORMS, BEING POSSIBLE TO NOTIFY DIFFERENT CONDITIONS OF CONTRAINDICATIONS FOR METHODS OR THE ENTIRE ACUPUNCTURE ### BEING ESSENTIAL NOW, IN ADDITION TO THE ZIP CODE, THE INTERNET FOR USE OF THE PROGRAM (ADJUSTMENT FOR OFFLINE USE BUT WITHOUT BENEFIT OF IMPLEMENT); ADEQUACY OF SMALL LOGICAL FUNCTION IMPLEMENTING NOTICE OF SHU USE BY TIME USING TEMPORAL VARIABLES OF THE PROGRAM AS OVERLAY MARKING CONSIDERING THE TIME TO FINISH PRESCRIPTION AND START ACUPUNCTURE AT THE PREDICTED TIME
### TAO 3.2: ADJUSTMENT OF THE ORINETATION OF PRESCRIPTION OBJECTS WITH NEW OPTIMIZED ALGORIOT FOR ARRANGEMENT OF ITEMS
### TAO 3.3: ADJUSTMENT FOR ENHANCED FUNCTIONS TO 6-SHI-NORMAL, 16-HUAN-DELAYED (BRADYCARDIC), 17-KOU-HOLLOW, 28-JI-ACcelerated OR 28-DA-LARGE, 1-FU-SURFACE PULSES FOR ANALYSIS OF SHANG HAN LUN ALGORITHMS
### TAO 3.4: EXTRA API IMPLEMENTATION (METEOSOURCE, SUN, PYOWN) FOR WEN BING XUE ANALYSIS ALGORITHM
### TAO 3.5: ADDITION OF WEN BING XUE WEATHER ANALYSIS FEATURES (SUMMERHEAT HEAT, DUMPHEAT, AUTUMN DRYNESS...)
### TAO 3.6: NEURAL NETWORK FOR WEB BING ANALYSIS PATHWAYS OF WU JU TONG AND YE TIAN SHI IN ADDITION TO SHANG HAN LUN AS DESCRIBED IN THE BOOK BY ZHANG ZHONG JING ALSO ANALYZING SUBTYPES OF SHANG HAN, ZHONG FENG, FENG WEN AND WEN BING ANALYSIS DEPENDENT ON PHYSICAL EXAMINATION WITH CONFIRMATION OF SYMPTOMS QUESTIONNAIRE TO EXPOSE PATHOLOGIES AND INTERPOLATION OF LISTS SEPARATED BY DIMIDIA
### TAO 3.7: REFORMULATION OF DIAGNOSTICS 229-252 (REGARDING SHANG HAN LUN WITH WENG BIN BUT WITH NOMENCLATURE ERRORS PREVENTING CORRECT LOCATION AND USE ACCORDING TO THE ORIGINAL THEORY OF ZHENG ZHONG JING'S BOOK) FUNCTIONS REPROGRAMMED FOR NEW DIAGNOSTICS (198-201 [YE TIAN SHI], 202-207 [SHANG HAN LUN], 195-197 AND 258-264 [WU JU TONG], 265-268 [SHANG HAN LUN SUBTYPES]) IN APPROPRIATE NOMENCLATURE FOR ANALYSIS. SOME CORRECTIONS IN THE LISTING DO NOT CORRESPOND TO THE ORIGINAL THEORY AND ARE DELETED. AFTER RELOCATION AND DELETION, EMPTY INDEXES WERE GENERATED BETWEEN 229-252 THE DIAGNOSES OF LOU CHANNEL AND JING JIN (MUSCLE TENDEND) PATHOLOGIES. ALSO RELOCATED DIAGNOSTICS 138-143 WHICH ORIGINALLY CORRESPONDED TO CANICULA BY CHANNELS (HOWEVER CANICULA CAN ONLY BE IN WEI AND NOT IN CANAL), CANICULA EXCHANGES UNIFIED IN DIAGNOSIS 238 AND OTHER LOCATIONS RENAMED IN NEW WEN BIN DE WAN SHE HE, BEING AS DESCRIBED AS ALREADY IN INTERDEPENDENCE BY FUNCTIONS BY OLD DIAGNOSES 229-232 (BEING REALLOCATED TO A NEW INDEX)
### TAO 3.8: STABLE VERSION (BUGS FIXES)
### TAO 3.9: AESTHETIC IMPROVEMENT WITH SYMBOLS AND SCREEN ADJUSTMENTS, TEXT CENTERING AND MARKING OF POINTS WITH SHORTER TIMES AND NEW EXPLANATORY TEXTS (SHORTENED) IN ADDITION OF ADJUSTED MTC MARKINGS FOR DEMONSTATIONS
### TAO 4.0: IMPLEMENTATION OF REMOTE RECORD READING PREVIOUSLY THERE WERE LOSSES DUE TO PRESCRIPTIONS NOT BEING SAVED DURING THE ACUPUNCTURE SESSION, CAN NOW BE SAVED AND REOPENED WITH EASY READING
### TAO 4.1: REFORMULATION OF DATABASES WITH RAW INSERTION INCLUDING PUNCH TYPE, RECOMMENDATIONS AND METHODS, IN ADDITION TO INCLUDING A VERSION OF THE PROGRAM IN RESCUE
### TAO 4.2: ADJUSTMENT OF THE READING SCREEN TO SEPARATE POINTS ACCORDING TO TYPES, CORRECTION OF MODULE D TREE, I.E. PRESCRIPTION MODULE WITHOUT EXAMINATION, ALREADY SABLE AND FUNCTIONAL WITH DB
### TAO 4.3: INSERTION OF NEW DATABASE WITH SENSITIVE DATA DUE TO EXCESSIVE FORMATTING OF THE PRESCRIPTION BASE WITH LOSSES NOW MINIMIZED (LOG ACCESS FOR IDENTIFICATION ONLY)
### TAO 4.4: CORRECTION OF ERROR IN CPFS WITH FINAL VALIDATOR ABOVE 9 CAUSING INVALIDITY, TABULATION CORRECTION AND STATEMENT TYPING ERRORS
### TAO 4.5: 03/2024 ADDITION OF QUANTITATIVE PULSE NUMBERING AND ADDITION OF CLI LINE GRAPH, ADDITION OF PULSE NUMBERING BY ANALYTIC FUNCTION FOR BETTER VIEW
### TAO 4.6: CONNECTION TEST ADJUSTMENT WITH IOS COMPILERS AND ADJUSTMENT OF INCOMPATIBLE UNICODES AND TABULATION IN USE AT PORTABLE DEVICES, GREATER TEMPORAL ENGINE CONTROL FOR CHRONOACUPUNCTURE (USE OF SHU SYSTEMS) WITH IMPROVED ALGORITHMS
### TAO 4.7: PATCH ADJUSTMENT FOR TIMEZONE BY PYTZ MODULE FOR BRAZIL LOCATION ACCORDING TO ERROR OBSERVED IN COMPILING VERSIONS AT GITHUB SERVER (CHANGED TIME) INSIDE VM OF SERVER
### TAO 5.0: NEW QUICK MODE OF ANALYSIS, SKIPING QUESTIONS  IF SELECTED (IN PROGRESSION). NEW DATA FORMATTING TO THE NEW AI DATABASE FOR COMPARATIVE TESTS BETWEEN SUPPORT VECTOR MACHINES AND LOGISTICAL DATA REGRESSION (NUMERICAL ANALYSIS IN THONG'S TYPE, CUNKOU, TYPES OF PULSES, COMPLETION AND DIAGNOSIS BEING USED FOR TONGUE AND TYPES OF PULSES ALPHABETICAL NUMBERS EXPONENTIATED AND SUMMED TO GENERATE DIFFERENCES OF SUMS FOR FURTHER AI ANALYSIS) AND EXPORTATION MODE INSIDE EACH USE. INSERTION OF HIDDEN NOTES OF NUMBERED ERRORS INSIDE PROGRAM (JUST FOR FATAL ERRORS) ALLOWING CORRECTIONS OF CODES
### TAO 5.0.1: UNSTABLE VERSION NOT WORKING AFTER MATH CALCS FOR DATA EXPORTS
### TAO 5.0.2: UNSTABEL VERSION PREVIOUS VERSION DESYNCHRONIZED INPUTS AND ATTEMPTED ADJUSTMENTS WITHOUT DOWNGRADE (VERSION 5.0.1), SUCCESSFULLY PATCH INSERTION IN TEST AND PINNED ADDRESS MODULE ADDED
### TAO 5.0.3: UNSTABLE VERSION TESTING PATHS OF MARKED OUTPUTS ERROR FOR QUICK MODE JUMPING HIDDEN LAYERS
### TAO 5.1: CORRECTION OF THE FOLLOWING PROBLEMS: ERROR REQUESTING ADDRESS WHEN USING PINPOINT DUE TO USE OF .CSV, FILE USING .TXT BECAUSE IT IS SINGLE LINE SOLVED PROBLEM; QUICK ERROR==TRUE DOESN'T SKIP THE QUESTIONNAIRE DUE TO DIFFERENCE CALCULATIONS, BLANK HDA IS DASHED , EXPORT2 GENERATED LIST AS STRING FOR DATABASE (MAILING THE TRAINING BASE IN THE FUTURE, ADDING INFORMATION ABOUT THE FOUR DATABASES IN THE INFO, FAST ADDRESS PINPOINT STORAGE MOVED FROM RAM TO FILE (BECOMING AVAILABLE IN SCRIPTS), EXPORT5 ERROR OUT 0 BECAUSE IT IS A FUNCTION OF PYTHON UNDERSTANDING, COMPLETED REGLOG/SVM TRAINING BASE TESTS, FROM THIS VERSION BEING SET FOR COLLECTION. RESPECTIVELY FOR ALGORITHM TRAINING BASIS ON THE DATA BELOW: EXPORT1=HIGH LANGUAGE (NUMBERED) SQUARED, 18 SEQUENTIAL NUMBERS CORRESPONDING TO ZHANG FU [EACH TYPE IN SUPERFICIAL, BLOOD LEVEL AND DEEP), IN SEQUENCE P(S/XUE/D)/BP(S/XUE/D)/PC(S/XUE/D)/C(S/XUE/D)/F(S/XUE/P)/R(S/XUE/D), EXPORT3=USING LETTERS CONVERTED TO NUMBERS AND SQUARED, EXPORT4=COMPLETION 1=C 2=BP 3=P 4=R 5=F 0=NO COMPLETION , EXPORT6(YES IT REALLY SKIPED!)=RENYNG EXAM 1=C 2=BP 3=P 4=R 5=F 0=NORMAL, EXPORT5=DIAGNOSTICS USE MAIN DX NUMBER OF THE PROGRAM AND NUMBER EXPONENTIATED TO THE SQUARE AND ADDED IF MORE THAN ONE (SUM OF EXPONENTIALS) (AVOIDS SIMULTANEITY OF SUMMED PRODUCTS, E.G. DX1+DX2+DX3=DX6 DX1+DX5 ALSO GIVES DX6 EVEN THOUGH THE OTHER DX IS, BUT EXPONENTIATED DIVERGENS: DX14 AND DX26, SEQUENTIALLY, DATA GOAL: USE IN SUPPORT MACHINE VECTORS OR REGLOG
### TAO 5.1.1: TEMPORAL CORRECTION OF SUMS AND SUBTRACTIONS IN 24H DAYS CAUSING NEGATIVE HOURS OR ABOVE 24H, INSERTION OF PULSE SPLITTING ALLOWING MASSIVE INSERTION SIMULTANEOUS WITH COLLECTION AND SYNCHRONOUS ANALYSIS IN PREVIOUS FUNCTIONS, IMPROVEMENTS IN CANDY EYE DESIGN EVEN IN CLI
### TAO 5.1.2: CORRECTION OF PROGRAM ERRORS RELATED TO DATABASE IMPLEMENTATION FOR AI INITIAL IMPLEMENTATION OF ARITHMETIC TESTS
### TAO 5.1.3: TABLE FIXES AND DESIGN CHOICES
### TAO 5.1.4: UNSTABLE IMPLEMENTED ARITHMETIC CALCULATIONS FOR DATABASE ANALYSIS
### TAO 5.1.5: STABLE VERSION WITH LOGIC IMPLEMENTATIONS THAT WORK, REMOVED OTHERS WITH ANOMALIES SUCH AS THIRD DEGREE ARITHMETIC FUNCTION IN DIAGNOSTIC LOOPS THAT GENERATED MEMORY OVERLOAD AND ERROR
### TAO 5.1.6: NEW ATTEMPT OF DIAGNOSTIC LOOP USING LESS MEMORY TO GENERATE THE LOOP, SINCE NO CODE ERROR WAS FOUND IN PREVIOUS ATTEMPTS AND DOWNGRADE OF THIS FUNCTION INTO A STABLE VERSION FOR NEW TESTING
### TAO 5.1.6a: WRITER FUNCTION ADJUSTMENT VIA PANDAS WITH NEW GLOBAL LIST TO INDEX SHORT LOOP OF DIAGNOSTICS USING COMPETITIVE PROCESSES
### TAO 5.2.0: SUCCESSFULLY DEPLOYED AND TESTED THE GENERATION OF A DATABASE FOR AI ALGORITHMS WITH INDIVIDUAL DIAGNOSTIC PARAMETERIZATION AND PARAMETERIZED IN FIVE FUNCTIONS AND SECOND DEGREE ARITHMETIC FUNCTIONS FOR AI CALCULATIONS IN USING NOT SUPERVISED CALCULATIONS FOR DIAGNOSTICS
### TAO 5.2.1: ADJUSTED ADDRESS ERROR DUE TO USING OUTDATED FILE AND AUTOMATICALLY GENERATING BLANK VALUE AND DATING ERROR DUE TO ALTERNATING DECADES WHEN DD/MM/YY DATES ARE PROVIDED
### TAO 5.2.2: IPHONE CONNECTION TEST IMPROVED (IOS), CORRECT THE LOGICAL FUNCTION MODIFYING PERSON'S NAME, WEN BING AND SHANG HANS TAB ADJUSTMENT
### TAO 5.2.3: FUNCTION ADJUSTMENT FOR IOS ERROR BY PYTHON FILE METHODS ON IOS
### TAO 5.2.4: BLOCKING THE USE OF PROGRAM WITHOUT A DATABASE DUE TO FATAL ERRORS AFTER IMPLEMENTATION OF DATA PROVIDED BY THEM AND NO LONGER REQUESTED TO RUN AS WELL AS TEMPORARY STORAGE OF STRINGS DURING EXECUTION WITHOUT USE OF RAM MEMORY TO AVOID LOSS OF INFORMATION TIME CONSUMING
### TAO 5.2.5: GENDER ADJUSTMENT FOR CALCULATIONS GENERATING 0 VALUES IN FEMALE, AGE OVERLAPPING FUNCTION ADJUSTMENT WITH THE SAME STRING IN USE GENERATING OVERLAPPED VALUES WITH ERRORS WHEN CALCULATING DATE EXPOSURE DD/MM/90 (1990 OR 2090?) NOW CALCULATING CORRECTLY, WITHDRAWAL ADJUSTMENT OF ITERATED PRESCRIPTIONS
### TAO 5.2.6: ADDED NEW DIAGNOSTIC ALGORITHM FOR DETECTIONS BY DATA, WHETHER USING: INT(2*C+(A-C)*3+C*2-8) == A=SURFACE PULSE AND C=DEEP PULSE, 1 (WEAK), 2 (REGULAR) AND 3 (STRONG) AS INPUTS AND RESULTS: 3=FULL HEAT, -1=EMPTY HEAT, 1=FULL COLD, -3=EMPTY COLD, 2=FULL HEAT, -4=EMPTY HEAT WITH COLLAPSE, 4=HEAT FULL WITH APOSTASY, -2=COLD EMPTY, 0= NORMAL PULSE EXAM == ; STATISTICS USIND ROUNDED DEFINITION OF COMPLETION MEDIAN FOR QUICK RESPONSE JUST IN CASE OF INDEFINITIONS; DYNAMIC VISUAL DISPLAY OF PRESCRIPTION METHOD AND SAVING DATA SCREEN
### TAO 5.2.7: NEW WU XING TEST FORMULARY IN CASES OF NO ANSWEAR FOR COMPLEITION TESTS
