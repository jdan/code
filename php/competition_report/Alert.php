<?php 

define('BASE_DIR', dirname(__FILE__) . '/'); 
date_default_timezone_set('America/New_York');

abstract class Alert {
	
	protected $config;
	protected $key;         // entry in the config 
	protected $con;         // DB connection handle
	protected $text;
	protected $debug;
	
	public function __construct($debug=false) {
		$this->debug = $debug;

		$config_file = BASE_DIR . 'config.ini';
		$this->config = parse_ini_file($config_file, true);
		
		$host = $this->config['database']['host'];
		$db   = $this->config['database']['database'];
		$user = $this->config['database']['username'];
		$pass = $this->config['database']['password'];
		
		$this->text = "";
		$this->key = get_class($this); // set ini entry to the class that needs it

		$s = "host=$host dbname=$db user=$user password=$pass";
		$this->con = pg_connect("host=$host port=5432 dbname=$db user=$user password=$pass");
		if (!$this->con) {
			die("Could not connect: " . pg_last_error() . "\n");
		}
	}
	
	public function sendAlert() {
		$this->generateAlert();
		// generate an array of addresses
		$addresses = $this->config[$this->key]['address'];
		$this->mailAlert($addresses);
	}
	
	protected function mailAlert($addresses) {
		if ($this->debug) {
			echo "Would have sent to:\n" . join("\n", $addresses);
			echo "Subject:\t" . $this->config[$this->key]['subject'] . ' ' . date("Y-m-d", strtotime("-1 week")) . "\n";
			echo "Body:\n" . $this->text . "\n";
		} else {
			$thisfile = 'file.csv';

			$encoded = chunk_split(base64_encode($this->text));

			// create the email and send it off

			$subject = $this->config[$this->key]['subject'] . ' ' . date("Y-m-d", strtotime("-1 week"));
			$from = $this->config[$this->key]['from'];
			$headers = 'MIME-Version: 1.0' . "\n";
			$headers .= 'Content-Type: multipart/mixed;
			    boundary="----=_NextPart_001_0011_1234ABCD.4321FDAC"' . "\n";

			$message = '

			This is a multi-part message in MIME format.

			------=_NextPart_001_0011_1234ABCD.4321FDAC
			Content-Type: text/plain;
			        charset="us-ascii"
			Content-Transfer-Encoding: 7bit

			

			------=_NextPart_001_0011_1234ABCD.4321FDAC
			Content-Type: application/octet-stream;  name="';

			$message .= "$thisfile";
			$message .= '"
			Content-Transfer-Encoding: base64
			Content-Disposition: attachment; filename="';
			$message .= "$thisfile";
			$message .= '"

			';
			$message .= "$encoded";
			$message .= '

			------=_NextPart_001_0011_1234ABCD.4321FDAC--

			';

			// now send the email
			mail(join(", ", $addresses), $subject, $message, $headers, "-f$from");
		}
	}
	
	abstract protected function generateAlert();

	// TODO should we clean up resources (db handle) in the destructor?
}
