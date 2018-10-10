package com.hw;

import java.awt.Font;
import java.io.IOException;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.CategoryAxis;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.title.TextTitle;
import org.jfree.data.category.DefaultCategoryDataset;

public class ReadFlie {

	public static void main(String[] args) throws IOException {
		Read rd = new Read();
		Map map=rd.Readflie();
		Set<String> values = map.keySet();
        Iterator<String> it = values.iterator();
        
        
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        while(it.hasNext()) {
        	String str =it.next();
        	dataset.setValue((Number) map.get(str), str, "IP地址");
        	
        }
		// 装载数据
		// 产生柱状图
		// JFreeChart chart = ChartFactory.createBarChart("标题", "x轴标志", "y轴标志",
		// 设置数据, 设置图形显示方向, 是否显示图形, 是否进行提示, 是否配置报表存放地址);

		// 3D柱状图
		JFreeChart chart = ChartFactory.createBarChart("日志分析", "ip", "访问次数",
				dataset, PlotOrientation.VERTICAL, true, true, false);
		// 解决中文乱码
		CategoryPlot plot = chart.getCategoryPlot();
		CategoryAxis domainAxis = plot.getDomainAxis();
		NumberAxis numberAxis = (NumberAxis) plot.getRangeAxis();

		TextTitle textTitle = chart.getTitle();
		textTitle.setFont(new Font("黑体", Font.PLAIN, 20));
		domainAxis.setTickLabelFont(new Font("sans-serif", Font.PLAIN, 11));
		domainAxis.setLabelFont(new Font("宋体", Font.PLAIN, 12));
		numberAxis.setTickLabelFont(new Font("sans-serif", Font.PLAIN, 11));
		numberAxis.setLabelFont(new Font("宋体", Font.PLAIN, 12));

		chart.getLegend().setItemFont(new Font("宋体", Font.PLAIN, 12));

		try {
			// 创建图形显示面板
			ChartFrame cf = new ChartFrame("柱状图", chart);
			cf.pack();
			// 设置图片大小
			cf.setSize(800, 600);
			// 设置图形可见
			cf.setVisible(true);
			// 保存图片到指定位置
			// ChartUtilities.saveChartAsJPEG(new File("C:\\bar.png"), chart,
			// 500,
			// 300);
		} catch (Exception e) {
			System.err.println("Problem occurred creating chart.");
		}

	}

}
