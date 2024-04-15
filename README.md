# DLS (Data Leak Site) Buster

This Python script enables secure downloading of datasets from active Data Leak Sites (DLS) listed on a public GitHub repository. It integrates user selection, Tor network access, and provides robust features such as download progress monitoring and resumable downloads.

## Features

- **Interactive DLS Selection**: Users can choose from a list of active DLS or enter a custom `.onion` URL.
- **Tor Network Integration**: Secure access to `.onion` sites via the Tor network.
- **Progress Monitoring**: Real-time download progress updates.
- **Resumable Downloads**: Ability to resume interrupted downloads, enhancing reliability.

## Prerequisites

Before you start using this script, you need to have the following installed:

- Python 3.x
- `requests`, `pandas`, `beautifulsoup4`, `tqdm` libraries
- Tor Browser or a Tor service running locally

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/dls-downloader.git
cd dls-downloader
```

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using:

```bash
python dls_downloader.py
```

Follow the on-screen prompts to select the DLS from which you wish to download data.

## Security Considerations

Ensure your actions comply with local laws and regulations regarding data access and privacy. Use this script responsibly and ethically.

## Contributing

Contributions to improve the script or add features are welcome. Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and research purposes only. The author is not responsible for misuse or for any damage that may occur. Always ensure that your actions are legal and authorized.
