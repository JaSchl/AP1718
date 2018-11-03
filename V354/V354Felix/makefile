all: Protokoll.pdf

Plotgedaempft.pdf:PlotsAuswertung2/Plotgedämpft.py
	python PlotsAuswertung2/Plotgedämpft.py
PlotUcUv.pdf     :PlotsAuswertung2/PlotUcUv.py
	python PlotsAuswertung2/PlotUcUv.py
PlotRes.pdf      :PlotsAuswertung2/PlotReslinearBreite.py
	python PlotsAuswertung2/PlotReslinearBreite.py
PlotPhiNu.pdf    :PlotsAuswertung2/Plotphinu.py
	python PlotsAuswertung2/Plotphinu.py
PlotPhiNuLin.pdf :PlotsAuswertung2/PlotPhiNuLinear.py
	python PlotsAuswertung2/PlotPhiNuLinear.py

Protokoll.pdf: Protokoll.tex Plotgedaempft.pdf PlotUcUv.pdf PlotRes.pdf  PlotPhiNu.pdf PlotPhiNuLin.pdf
	lualatex Protokoll.tex
	biber Protokoll.bcf
	lualatex Protokoll.tex
	make clean

clean:
	rm Plotgedaempft.pdf PlotUcUv.pdf PlotRes.pdf PlotPhiNu.pdf PlotPhiNuLin.pdf
	rm Protokoll.aux
	rm Protokoll.bbl
	rm Protokoll.bcf
	rm Protokoll.blg
	rm Protokoll.log
	rm Protokoll.run.xml
	rm Protokoll.toc

.PHONY: all clean
